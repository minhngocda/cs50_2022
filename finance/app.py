import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime, timezone

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def own_shares():
    """Helper function: Which stocks the user owns, and numbers of shares owned. Return: dictionary {symbol: qty}"""
    user_id = session["user_id"]
    owns = {}
    query = db.execute("SELECT symbol, shares FROM orders WHERE user_id = ?", user_id)
    for q in query:
        symbol, shares = q["symbol"], q["shares"]
        owns[symbol] = owns.setdefault(symbol, 0) + shares
    # filter zero-share stocks
    owns = {k: v for k, v in owns.items() if v != 0}
    return owns

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    owns = own_shares()
    total = 0
    for symbol, shares in owns.items():
        result = lookup(symbol)
        name, price = result["name"], result["price"]
        stock_value = shares * price
        total += stock_value
        owns[symbol] = (name, shares, usd(price), usd(stock_value))
    cash = db.execute("SELECT cash FROM users WHERE id = ? ", session["user_id"])[0]['cash']
    total += cash
    return render_template("index.html", owns=owns, cash= usd(cash), total = usd(total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if not request.form.get("symbol"):
        return apology("mising symbol", 400)
    if not request.form.get("shares"):
        return apology("missing shares", 403)

    result = lookup(request.form.get("symbol"))
    if not result:
        return apology("invalid symbol", 400)
        """return render_template("buy.html", invalid=True, symbol = request.form.get("symbol"))"""

    name = result["name"]
    price = result["price"]
    symbol = result["symbol"]
    shares = int(request.form.get("shares")) #convert str to int
    user_id = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']
    # check if user can afford the purchase
    remain = cash - price * shares
    if remain < 0:
        return apology("can't afford.", 400)

    # deduct order cost from user's remaining balance (i.e. cash)
    db.execute("UPDATE users SET cash = ? WHERE id = ?", remain, user_id)

    db.execute("INSERT INTO orders (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", user_id, symbol, shares, price, datetime.now())

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT symbol, shares, price, timestamp FROM orders WHERE user_id = ?", session["user_id"])
    return render_template("history.html", rows= rows)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        """result_check = is_provided("symbol")
        if result_check is not None:
        return result_check"""
        symbol = request.form.get("symbol")
        result = lookup(symbol)
        if not result:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", name = result["name"], price = usd(result["price"]), symbol = result["symbol"])

    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        pass
    else:
        return render_template("register.html")
    # check username and password
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if username == "" or len(db.execute('SELECT username FROM users WHERE username = ?', username)) > 0:
        return apology("Invalid Username: Blank, or already exists")
    if password == "" or password != confirmation:
        return apology("Invalid Password: Blank, or does not match")
    # Add new user to users db (includes: username and HASH of password)
    db.execute('INSERT INTO users (username, hash) \
            VALUES(?, ?)', username, generate_password_hash(password))
    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)
    # Log user in, i.e. Remember that this user has logged in
    session["user_id"] = rows[0]["id"]
    # Redirect user to home page
    return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    owns = own_shares()
    if request.method == "GET":
        return render_template("sell.html", owns = owns.keys())

    symbol = request.form.get("symbol")
    shares = int(request.form.get("shares")) # Don't forget: convert str to int
    # check whether there are sufficient shares to sell
    if owns[symbol] < shares:
        return apology("too many shares", 400)
        """return render_template("sell.html", invalid=True, symbol=symbol, owns = owns.keys())"""
    # Execute sell transaction: look up sell price, and add fund to cash,
    result = lookup(symbol)
    user_id = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']
    price = result["price"]
    remain = cash + price * shares
    db.execute("UPDATE users SET cash = ? WHERE id = ?", remain, user_id)
    # Log the transaction into orders
    db.execute("INSERT INTO orders (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", \
                                     user_id, symbol, -shares, price, datetime.now())

    return redirect("/")

from cs50 import get_float

def main():
    cash = get_input() * 100
    a = cash // 25
    b = cash % 25
    c = b // 10
    d = b % 10
    e = d // 5
    f = d % 5
    out_put = sum(a,c, e, f)
    print(out_put)


def get_input():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0:
                break
        except ValueError:
            print("That's not desired value!")
    return n

main()
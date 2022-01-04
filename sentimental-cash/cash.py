from cs50 import get_float

def main():
    cash = round(get_input(), 2)
    print(cash)


def get_input():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0:
                break
        except ValueError:
            print("That's not desired value!")
main()
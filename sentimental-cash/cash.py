from cs50 import get_float

def main():
    cash = get_input() * 100
    a = cash // 25
    b = 


def get_input():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0:
                break
        except ValueError:
            print("That's not desired value!")
main()
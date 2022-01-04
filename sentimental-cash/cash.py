from cs50 import get_float
def get_input():
    while True:
        try:
            n = float("Change owed: ")
            if n > 0:
                break
        except ValueError:
            print("That's not desired value!")
get_input()
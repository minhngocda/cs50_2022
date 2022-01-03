def main():
    height = get_height()
    for i in range(height):
        for k in range(height - i + 1):
            print(' ', end="")
        for l in range(i +1):
            print("#", end="")
        print(" ")

def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0 and n <9:
            break
    return n
main()


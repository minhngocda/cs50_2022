def main():
    height = get_height()
    for i in range(height):
        #to print space
        for k in range(height - i + 1):
            print('', end="")
        #to print # and do not break to new line
        for l in range(i +1):
            print("#", end="")
        #to print a new line
        print(" ")

def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0 and n <9:
            break
    return n
main()


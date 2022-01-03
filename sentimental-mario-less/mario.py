def main():
    height = get_height()
    for i in range(height):
        for k in range(height - i):
            print(' ')
        for l in range(i):
            print("#")
        print("\n")

def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0 and n <9:
            break
    return n
main()


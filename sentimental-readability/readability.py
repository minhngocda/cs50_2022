from cs50 import get_string

def main():
    x = get_input()
    count_letter = 0
    for i in x:
        if i.isalpha():
            count_letter += 1
    print(count_letter)


def get_input():
    answer = get_string("Text: ")
    return answer

main()
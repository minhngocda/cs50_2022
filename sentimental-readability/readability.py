from cs50 import get_string

def main():
    count_letter(get_input())
    print

def count_letter(x):
    #x = get_input()
    count_letter = 0
    for i in x:
        if i.isalpha():
            count_letter += 1
    return count_letter

#def count_words():



def get_input():
    answer = get_string("Text: ")
    return answer

main()
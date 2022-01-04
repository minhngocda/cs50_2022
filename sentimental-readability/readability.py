from cs50 import get_string

def main():
    x = count_letter(get_input())

def count_letter(x):
    #x = get_input()
    count_letter = 0
    for i in x:
        if i.isalpha():
            count_letter += 1
    return count_letter

def count_words(x):
    count_word = 0
    for i in x:
        if i = " "
            count_word += 1



def get_input():
    answer = get_string("Text: ")
    return answer

main()
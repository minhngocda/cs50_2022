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
    word = 0
    count_space = 0
    for i in x:
        if i = " ":
            count_space += 1
    if count_space =! 0:
        word = count_space + 1
    else:
        if count_letter(x) > 0:
            word = 1
    return word





def get_input():
    answer = get_string("Text: ")
    return answer

main()
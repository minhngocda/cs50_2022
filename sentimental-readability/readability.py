from cs50 import get_string

def main():
    text = get_input()
    x = count_letter(text)
    y = count_words(text)
    z = count_sentence(text)
    L = x / y * 100
    S = z / y * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    print (index)
    a = round(index,0)
    if a < 1:
        print("Before Grade 1")
    elif a > 16:
        print("Grade 16+")
    else:
        print("Grade ", a)
    #print( x )
    #print(L)
    #print(S)

def count_letter(x):
    count_letter = 0
    for i in x:
        if i.isalpha():
            count_letter += 1
    return count_letter

def count_words(x):
    word = 0
    count_space = 0
    for i in x:
        if i == " ":
            count_space += 1
    if count_space != 0:
        word = count_space + 1
    else:
        if count_letter(x) > 0:
            word = 1
    return word

def count_sentence(x):
    sentence = 0
    a = x.count('.')
    b = x.count('?')
    c = x.count('!')
    sentence = a + b + c
    return sentence


def get_input():
    answer = get_string("Text: ")
    return answer

main()
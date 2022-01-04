from cs50 import get_string

def main():
    x = count_letter(get_input())
    #L = count_words(get_input())
    #S = count_sentence(get_input())
    print( x )
    #print( L + ' words')
    #print( S + ' sentences')

def count_letter(x):
    count_letter = 0
    for i in x:
        if i.isalpha():
            count_letter += 1
    return count_letter

#def count_words(x):
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

#def count_sentence(x):
    sentence = 0
    for i in x:
        if i.isalpha() and (str(i+1) == '.' or str(i+1) == '!' or str(i+1) == '?'):
            sentence += 1
    return sentence


def get_input():
    answer = get_string("Text: ")
    return answer

main()
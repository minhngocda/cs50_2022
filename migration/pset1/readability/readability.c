#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int count_letter(string text);
int count_word(string text);
int count_sentence(string text);

int main(void)
{//Get input text from user
    string input = get_string("Text: ");

    int input_letter = count_letter(input);
    //printf("%i letter(s)\n", input_letter);
    int input_word = count_word(input);
    //printf("%i word(s)\n", input_word);
    int input_sentence = count_sentence(input);
    //printf("%i sentence(s)\n", input_sentence);

     float L = input_letter *100.00 / input_word;
     float S = input_sentence *100.00 / input_word;

     float index = 0.0588 * L - 0.296 * S - 15.8;
     int x = round(index);
     if (x < 1)
     {
         printf("Before Grade 1\n");
     }
     else if (x > 16)
     {
         printf("Grade 16+\n");
     }
     else
     {
         printf("Grade %i\n", x);
     }
}

int count_letter(string text)
//check whether a character is alphabetical, then count it
{
    int letter = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if isalpha(text[i])
        {
            letter = letter + 1;
        }
    }
    return letter;
}

int count_word(string text)
//count spaces in text, assume that that a sentence will not start or end with a space,and a sentence will not have multiple spaces in a row.
{
    int space = 0;
    int word = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if isspace(text[i])
        {
            space = space + 1;
        }
    }
    if (space != 0)
    {
        word = space + 1;
    }
    else
    {
        if (count_letter(text) > 0)
        {
            word = 1;
        }
    }
    return word;
}

int count_sentence(string text)
//check whether a character is alphabetical end with (.)(?)(!), then count it as a sentence
{
    int sentence = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]) && (text[i+1] == '.' || text[i+1] == '?' || text[i+1] == '!'))
        {
            sentence = sentence + 1;
        }
    }
    return sentence;
}
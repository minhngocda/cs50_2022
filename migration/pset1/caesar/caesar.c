#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int convert_argv_to_int (string);
string get_plain_text (void);
void convert_ciphertext (string text, int key);

int main(int argc, char *argv[])
{
    int j = 0;
//Check that program was run with one command-line argument
    if(argc != 2 )
    {
        printf("Usage: %s key\n", argv[0]);
        exit(1);
    }
    else
    {
//Iterate over the provided argument to make sure all characters are digits
        for (int i = 0 ; i < strlen(argv[1]) ; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: %s key\n", argv[0]);
                exit(1);
            }
            else
            {
                j++;
            }
        }
    int n = convert_argv_to_int (argv[1]);
    string PlainText = get_plain_text();
    printf("ciphertext: ");
    convert_ciphertext (PlainText, n);
    //Print a newline
    printf("\n");
    }
}
//Convert that command-line argument from a string to an int
int convert_argv_to_int (string text)
{
    return atoi (text);
}

//Prompt user for plaintext
string get_plain_text (void)
{
    string n = get_string("plaintext: ");
    return n;
}

//Iterate over each character of the plaintext:
//If it is an uppercase letter, rotate it, preserving case, then print out the rotated character
//If it is a lowercase letter, rotate it, preserving case, then print out the rotated character
//If it is neither, print out the character as is

void convert_ciphertext (string text, int k)
{
    for (int i = 0; i < strlen(text); i++)
    {
        int a = text[i] + k % 26;
        if isupper(text[i])
        {
            if (a > 90)
            {
                a = a - 26;
                printf("%c", a);
            }
            else
            {
                printf("%c", a);
            }
        }
        else if islower(text[i])
        {
            if (a > 122)
            {
                a = a - 26;
                printf("%c", a);
            }
            else
            {
                printf("%c", a);
            }
        }
        else
        {
            printf("%c", text[i]);
        }
    }
}
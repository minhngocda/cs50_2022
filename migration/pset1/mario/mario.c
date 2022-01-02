#include <cs50.h>
#include <stdio.h>

int input;

int get_positive_int(void);

int main(void)

{
    input = get_positive_int();
    // i to make new line
    for (int i = 0; i < input; i++)
    {
        // k to print space
        for (int k = 1; k < input - i; k++)
        {
            printf(" ");
        }
        //j to print #
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

// this function to get input from 1 to 8
int get_positive_int(void)
{
    int i;
    do
    {
        i = get_int("Height: ");
    }
    while (i < 1 || i > 8);
    return i;
}
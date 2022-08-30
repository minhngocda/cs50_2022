#include <cs50.h>
#include <stdio.h>
#include <math.h>
float get_input(void);

int main(void)
{
    int i = 0;
    int k = 0;
    int l = 0;
    int m = 0;

    float dollar = get_input();
    int a = round(dollar * 100);

    if (a >= 25)
    {
        i = a / 25;
        a = a - 25 * i;
    }

    if (a >= 10)
    {
        k = a / 10;
        a = a - 10 * k;
    }

    if (a >= 5)
    {
        l = a / 5;
        a = a - 5 * l;
    }

    if (a >= 1)
    {
        m = a / 1;
    }


    printf("%i\n", i + k + l + m);
}


float get_input(void)
{
    float i;
    do
    {
        i = get_float("Change owed: ");
    }
    while (i < 0);
    return i;
}
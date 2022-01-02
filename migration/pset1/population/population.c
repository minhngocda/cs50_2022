#include <cs50.h>
#include <stdio.h>


int StartSize;
int EndSize;
int Year;


void getStartSize(void)
{
    do
    {
        StartSize = get_int("Start size: ");
    }
    while (StartSize < 9);
}

void getEndSize(void)
{
    do
    {
        EndSize = get_int("End size: ");
    }
    while (EndSize < StartSize);

}

int calculateYear(void)
{
    int x = 0;
    int CurrentSize = 0;
    // 2 cases, if EndSize = StartSize, then x = 0, if EndSize different from StartSize, then do the calculation, return x as Year
    if (EndSize != StartSize)
    {
        do
        {
            CurrentSize = StartSize + StartSize / 3 - StartSize / 4 ;
            StartSize = CurrentSize;
            x++;
        }
        while (CurrentSize < EndSize);
    }
    printf("Years: %i", x);
    return x;
}

int main(void)
{
    // TODO: Prompt for start size
    getStartSize();
    // TODO: Prompt for end size
    getEndSize();
    // TODO: Calculate number of years until we reach threshold
    calculateYear();
}
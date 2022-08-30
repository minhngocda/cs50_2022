// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t header[HEADER_SIZE];
    /* There is only one header, so parse it just once */
    if (fread(&header[0], sizeof(header), 1, input))
    {
        fwrite(&header[0], sizeof(header), 1, output);
    }

    // TODO: Read samples from input file and write updated data to output file
    /* Assuming 16-bit signed integer PCM payload */
    int16_t sample;
    while (fread(&sample, sizeof(sample), 1, input))
    {
        /* Round value to nearest number */
        double scaledValue = sample * factor;

    /* Clamp new value */
        if (scaledValue >= INT16_MAX)
        {
            sample = INT16_MAX;
        }
        else if (scaledValue <= INT16_MIN)
        {
            sample = INT16_MIN;
        }
        else
        {
            sample = (int16_t)scaledValue;
        }
        fwrite(&sample, sizeof(sample), 1, output);
    }
    // Close files
    fclose(input);
    fclose(output);
}

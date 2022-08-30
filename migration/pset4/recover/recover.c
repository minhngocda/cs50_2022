#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// Number of bytes in a block
const int BLOCK_SIZE = 512;
// define BYTE struct, contain 8 bit, or 1 byte
typedef uint8_t  BYTE;

int main(int argc, char *argv[])
{
//Check exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }
//open argument to read
    FILE *input_file = fopen(argv[1], "r");
// check if file cannot be opened for reading

    if (input_file == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 1;
    }
//

    BYTE buffer[BLOCK_SIZE];
    FILE *output_file = NULL;
    char file_name [8];
    int count = 0;

    while (fread(&buffer, BLOCK_SIZE, 1, input_file) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) ==  0xe0)
        {
// If not first JPEG, close previous
            if (!(count == 0))
            {
                fclose(output_file);
            }
// Initialise file
            sprintf(file_name, "%03i.jpg", count);
            output_file = fopen(file_name, "w");
            count++;
        }

// If JPEG has been found, write to file
        if (!(count == 0))
        {
            fwrite(&buffer, BLOCK_SIZE, 1, output_file);
        }
    }
    fclose(input_file);
    fclose(output_file);
    return 0;
}
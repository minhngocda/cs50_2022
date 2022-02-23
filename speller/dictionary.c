// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1] * 'z';
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    for(int i = 0; i<strlen(word);i++)
    {
        sum += word[i];
    }
    return (sum % N);
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open the dictionary
    FILE *file = fopen(dictionary,"r");
    if (file == NULL)
    {
        return false;
    }

    //read one by one word
    char word[LENGTH + 1]
    while (fscanf(file,%s, word)!= EOF )
    {
        //create new node
        node *new_node = malloc(sizeof(node));
        IF (new_node == NULL)
        {
            return false;
        }
        // copy over the word
        strcpy(n->word, word);
        new_node->next = NULL;

        int index = hash(word);
        if(table[index] == NULL)
        {
            table[index] = new_node;
        }
        else
        {
            new_node->next = table[index];
            table[index] = new_node;
        }
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}

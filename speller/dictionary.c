// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
int total_word=0;
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);

    node *cursor = table[index];
    while (cursor != NULL)
    {
        if(strcasecmp(cursor->word, word)==0)
        {
            return true;
        }
        cursor = cursor->next;
    }

}

// Hashes word to a number
unsigned int hash(const char *word)
{
// TODO: Improve this hash function
    int sum = 0;
    for(int i = 0; i<strlen(word);i++)
    {
        sum += tolower(word[i]);
    }
    return (sum % N);
  //  return toupper(word[0]) - 'A';
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
        total_word++;
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total_word;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // print link list
    for (int i = 0; i<N; i++)
    {
        node *head = table[i];
        node *cursor = head;
        node *tmp = head;

        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}

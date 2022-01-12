import csv
from sys import argv , exit


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    STRs = []
    profiles = []
    # TODO: Read database file into a variable
    with open (argv[1], mode = 'r') as databases:
        reader = csv.DictReader(databases)
        STRs = reader.filenames[1:]
        for row in reader:
            profiles.append(row)

    # Initialise dictionary for sequence file
    seq_str_count = dict.fromkeys(STRs, 0)

    # TODO: Read DNA sequence file into a variable
    with open (argv[2], mode = 'r') as sequences:
        # Grab first line of txt file
        sequence = sequences.readline()

        # Loop over every STR from the database
        for STR in STRs:
            # Update the Sequence STR dictionary with max amount of repeats
            seq_str_count[STR] = longest_match(sequence, STR)


    # TODO: Find longest match of each STR in DNA sequence
    for profile in profiles:
        match_count = 0

    for STR in STRs:
            if int(profile[STR]) != seq_str_count[STR]:
                continue
            match_count += 1

    if match_count == len(STRs):
        print(profile['name'])
        exit(0)

    print("No match")
    exit(1)

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

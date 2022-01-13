import csv
from sys import argv

with open(argv[1], "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['title'])
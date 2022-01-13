import csv
from sys import argv

with open("small.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["title"])
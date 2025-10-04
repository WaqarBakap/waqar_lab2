import csv
import random


file = open("books-en.csv", encoding="latin-1")
reader = csv.DictReader(file, delimiter=";")


books = list(reader)


sample_books = random.sample(books, 20)


with open("bibliography.txt", "w", encoding="utf-8") as out:
    for i, row in enumerate(sample_books, start=1):
        author = row["Book-Author"]
        title = row["Book-Title"]
        year = row["Year-Of-Publication"]

        # format: Author. Title - Year
        line = f"{i}. {author}. {title} - {year}"
        out.write(line + "\n")

print("Bibliography saved to 'bibliography.txt'")

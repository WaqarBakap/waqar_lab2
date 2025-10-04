import csv

 
file = open("books-en.csv", encoding="latin-1")
reader = csv.DictReader(file, delimiter=";")


author_name = input("Enter author name: ")

print("\nBooks by", author_name, "from 1991 to 1996:\n")


for row in reader:
    author = row["Book-Author"]
    year = row["Year-Of-Publication"]


    if year.isdigit():
        year = int(year)
        if author_name.lower() in author.lower() and year in (1991,1996):
            print(author, "-", row["Book-Title"], "(", year, ")")

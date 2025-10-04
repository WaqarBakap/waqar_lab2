import csv


file = open("books-en.csv", encoding="latin-1")
reader = csv.DictReader(file, delimiter=";")


publishers = set()   # unique values
for row in reader:
    publishers.add(row["Publisher"])


print("Unique publishers in books-en.csv:")
for pub in publishers:
    print(pub)
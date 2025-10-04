import csv


with open("books-en.csv", encoding="latin-1") as file:
    reader = csv.DictReader(file, delimiter=";")   

    count = 0
    for row in reader:
        title = row["Book-Title"]   
        if len(title) > 30:
            count += 1

print("Number of titles longer than 30 characters:", count)

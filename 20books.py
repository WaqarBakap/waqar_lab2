import csv


with open("books-en.csv", encoding="latin-1") as f:
    reader = csv.DictReader(f, delimiter=";")
    books = []

   
    for row in reader:
        downloads = int(row["Downloads"] or 0)  
        books.append([row["Book-Title"], row["Book-Author"], downloads])


books.sort(key=lambda x: x[2], reverse=True)


print("Top 20 Books:")
for i in range(20):
    title, author, downloads = books[i]
    print(i+1, author, "-", title, ":", downloads, "downloads")

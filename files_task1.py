import csv

with open("students.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "score"])
    writer.writerow(["Ruslan", 25, 90])
    writer.writerow(["Aida", 22, 85])
    writer.writerow(["Daniyar", 24, 95])

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])
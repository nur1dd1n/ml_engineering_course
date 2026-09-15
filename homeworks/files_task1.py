import csv

# with open("students.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age", "score"])
#     writer.writerow(["Ruslan", 25, 90])
#     writer.writerow(["Nurslan", 22, 85])
#     writer.writerow(["Surlan", 24, 95])

# with open("students.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["name"])


def read_init(filename):
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
       for line in file:
            try: 
                numbers.append(float(line.strip()))
            except ValueError:
                pass
    return numbers

print(read_init("students.csv"))

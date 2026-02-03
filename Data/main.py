import csv

with open("Data/config.txt", "r", encoding="utf-8") as file:
    min_score = int(file.read().strip())

with open("Data/students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["score"] = int(row["score"])







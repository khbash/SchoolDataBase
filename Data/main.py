import csv
import json

with open("Data/config.txt", "r", encoding="utf-8") as file:
    min_score = int(file.read())

retest_list = []
with open("Data/students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["score"] = int(row["score"])
            if row["score"] < min_score:
                retest_list.append(row)

with open("Data/retest.csv", "w", encoding="utf-8") as  file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "surname", "score"])
    writer.writeheader()
    writer.writerows(retest_list)


success_list = []
with open("Data/students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["score"] = int(row["score"])
            if row["score"] >= min_score:
                row["passed"] = True
                success_list.append(row)

with open("Data/best_students.json", "w", encoding="utf-8") as file:
    json.dump(success_list, file, ensure_ascii=False, indent=4)








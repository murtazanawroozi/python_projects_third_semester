import csv
rows = [
    [101, "Ahmad", "SE"],
    [102, "Sara", "CS"]
]
with open(
    "students.csv", "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "department"])
    writer.writerows(rows)
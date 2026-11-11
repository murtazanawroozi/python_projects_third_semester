import json
student = {
    "id": 101,
    "name": "Ahmad",
    "courses": ["Python", "Database"]
}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(
        student,
        file,
        ensure_ascii=False,
        indent=2
    )

with open(
    "sample.txt",
    "r",
    encoding="utf-8"
) as file:
    first = file.read(5)
    file.seek(0)
    again = file.read(5)
    print(first, again)
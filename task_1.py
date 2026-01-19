
import json

# TODO решите задачу
def task(filename: str) -> float:
    summa = 0
    with open(filename) as file:
        data = json.load(file)
        for elem in data:
            summa += elem["score"] * elem["weight"]
    return  f"{summa:.{3}f}"

print(task("input.json"))

import json

import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

        with open(OUTPUT_FILENAME, 'w') as file_1:
            json.dump(data, file_1, indent=4, ensure_ascii=True)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

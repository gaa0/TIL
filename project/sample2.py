import csv

with open('avengers.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    # 한줄씩 읽는다.
    for row in reader:
        print(row['name'])
        print(row['gender'])
        print(row['appearances'])
        print(row['years since joining'])
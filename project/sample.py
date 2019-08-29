import csv

avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    },
    {
        "name": "thor odinson",
        "gender": "male",
        "appearances": 2402,
        "years since joining": 52
    },
    {
        "name": "steven rogers",
        "gender": "male",
        "appearances": 3458,
        "years since joining": 51
    }
]

with open('avengers.csv', 'w', newline='', encoding='utf-8') as f:
    #1. 저장할 데이터들의 필드 이름을 미리 지정한다.
    fieldnames = ['name', 'gender', 'appearances', 'years since joining']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    #2. 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()

    #3. dictionary를 순회하며(돈다!) key에 해당하는 value를 한줄씩 작성한다.
    for avenger in avengers:
        writer.writerow(avenger)
import json

# чтение данных
with open("src\datas\listusers.json",encoding='UTF-8') as file:
    data = json.load(file)

for i in data:
    print()
    for j in i.keys():
        print(j, ":", i[j])
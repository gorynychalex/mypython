import json

string='{"id":765, "email":"ivanov@mail.ru","surname":"Иванов","age":45,"friends":[123,456,789]}'

def encode(s = string, files = 'src\datas\data.json'):
    data = json.loads(string)

    with open(files,'w',encoding='UTF-8') as file:
        json.dump(data,file)
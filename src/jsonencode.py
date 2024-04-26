import json

user1= {'id': 1, 'name': 'Алексей', 'email': 'alexey@mail.ru', 'phones': [123456, 789012], 'admin': True}
user2= {'id': 2, 'name': 'Вася', 'email': 'vasya@mail.ru', 'phones': [8765, 9987], 'admin': False}

listusers=[user1,user2]

with open("src\datas\listusers.json","w",encoding='UTF-8') as file:
    data = json.dump(listusers,file)

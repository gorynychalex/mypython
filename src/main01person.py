from person import Person

# Создание объектов       
obj1 = Person()
obj2 = Person()

obj1.name = 'Bob'
obj1.money = 150

obj2.name = 'Masha'

obj1.out()
obj2.out()
obj1.changemoney(150)
obj1.out()
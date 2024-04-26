from datetime import date

print(__name__)

# Создание класса
class Person():
    counter=0
    car=list()

    # def __new__(cls, *args,**kwargs):
    #     print("вызов __new__ для ",str(cls))
    #     return super().__new__(cls)

    def __init__(self,name="",money=0) -> None:
        Person.counter += 1
        self.id=Person.counter
        self.__name=name
        self._money=money
        print("Создан ",self.__str__())

    @staticmethod
    def getCounter():
        print("Всего объектов ", Person.counter)

    def __privateMethod(self):
        print("Закрытый метод")

    def changename (self,newname):
        self.__name = newname
        self.out()

    def changemoney (self,newmoney):
        self._money = newmoney
        print(self.__str__())

    def setCar(self,car):
        self.car.append(car)

    def __str__(self):
        s = "Пользователь: " + self.__name + " c " + str(self._money) + " рублями."
        if len(self.car) > 0:
            s += "\n есть в наличии автомобили: "
            for i in self.car:
                s += "\n" + i.__str__()
        return s

class Student(Person):
    school=""
    group=""
    year_input=""

class Car():
    counter=0
    def __init__(self,name="",year=0) -> None:
        Car.counter += 1
        self.id=Car.counter
        self.name=name
        self.year=year
        print("Создан ",self.__str__())
    def __str__(self):
        return "Автомобиль: " + self.name + ', ' + str(self.year.year)
    


def main():
    person1=Person("Вася",30)

    student1 = Student("Олег",100)
    
    # print(person1.getName())

    car1=Car('Nissan',date(2005,1,1))
    person1.setCar(Car('Toyota',date(2020,1,1)))
    person1.car.append(Car('Toyota',date(2020,1,1)))
    person1.car.append(Car('BMW',date(1999,1,1)))

    print(person1)

if __name__ == "__main__":
    main()

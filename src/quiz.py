# Викторина

class Quiz():
    questions=list()
    name=""


class Question():
    counter=0
    listanswers=list()
    def __init__(self,qtext="",listanswers=list()) -> None:
        Question.counter += 1
        self.id=Question.counter
        self.text=qtext
        self.listanswers=listanswers
        

class Answer():
    counter=0
    def __init__(self,text="",correct=False) -> None:
        Answer.counter += 1
        self.id=Answer.counter
        self.correct=correct
        self.text=text

class Statistics():
    tests=list()
    pass

if __name__ == "__main__":
    q1=Question("Столица России",
                [Answer("Магадан"),
                 Answer("Москва",True),
                 Answer("Мурманск")])
    q2=Question("Столица Италии",
                [Answer("Рим",True),
                 Answer("Париж"),
                 Answer("Прага")])
    questions1=list([q1,q2])

    # Запуск опроса
    for q in questions1:
        print("\n",q.text,":")
        answer_counter=0
        for j in q.listanswers:
            answer_counter+=1
            print(answer_counter,") ",j.text)
            
        id=int(input("Ответ:"))
        if q.listanswers[id-1].correct:
            print("Верно!")
        else:
            print("Неверно!")


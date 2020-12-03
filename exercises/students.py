class Students:

    class_ = "student"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def avg_score(self, score1, score2, score3):
        print((score1 + score2 + score3)/3)

John = Students("John",14)

print(John.class_)

John.avg_score(70,80,90)

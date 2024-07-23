class  Assignment:

    def __init__(self, name, weight, score):
        self.__weight = weight
        self.__name = name
        self.score = score


    def __str__(self):
        return f"{self.__name} holds {self.__weight} weight with a score of {self.score}"
    
    def return_obj_weight(self):
        return self.__weight
    
class  Homework(Assignment):
    pass

class  Quiz(Assignment):
    pass

class  Test(Assignment):
    pass





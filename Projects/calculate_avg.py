class  Assignment:

    def __init__(self, name, weight, score):
        self.__weight = weight
        self.__name = name
        self.score = score


    def __str__(self):
        return f"{self.__name} holds {self.__weight} weight with a score of {self.score}"
    
    def return_description(self):
        print(f"{self.__name} ")
    
class  Homework(Assignment):
    pass

class  Quiz(Assignment):
    pass

class  Test(Assignment):
    pass
    
class Average:
    
    def __init__(self):
        pass

    def grab_average(self, nums_list):
        totals = 0
        total_nums = 0

        for num in nums_list:
            totals += num
            total_nums += 1

        avg = totals / total_nums

        return avg




class  Assignment:

    def __init__(self, name, weight, score):
        self.__weight = weight
        self.__name = name
        self.score = score


    def __str__(self):
        return f"{self.__name} holds {self.__weight} weight with a score of {self.score}"
    
    def return_obj_weight(self):
        return self.__weight
    
    def generate_master_list(self):
        # Create a master list to store objects created for quiz, hw, test, assign TYPE ASSIGNMENT objects
        my_quiz_objs = []
        my_assign_objs = []
        my_test_objs = []
        my_hw_objs = []
        my_master_obj_list = [my_assign_objs, my_hw_objs, my_quiz_objs, my_test_objs]
        my_master_class_list = [Assignment, Homework, Quiz, Test]
        nums = 0

        # Gather input from the user:
        for assignment_type in my_master_obj_list:
            
            if assignment_type == my_assign_objs:
                my_name = "Assignment"
                my_weight = 0.1

            elif assignment_type == my_hw_objs:
                my_name = "HW"
                my_weight = 0.2

            elif assignment_type == my_quiz_objs:
                my_name = "Quiz"
                my_weight = 0.3

            elif assignment_type == my_test_objs:
                my_name = "Test"
                my_weight = 0.4

            nums_to_add = int(input(f"Please type the number of {my_name} objects you would like to create: \n"))

            for i in range(nums_to_add):
                my_score = float(input(f"Please enter the score for {my_name} #{i+1}: \n"))
                my_obj_to_add = my_master_class_list[nums](my_name, my_weight, my_score)
                assignment_type.append(my_obj_to_add)
            
            nums += 1

        return my_master_obj_list
    
    def calculate_average(obj_list):
        sum = 0 
        my_stored_weight = 0

        for object_type in obj_list:
            my_stored_weight += object_type[0].return_obj_weight()
            
            for object in object_type:
                my_obj_weight = object.return_obj_weight()
                sum += object.score * my_obj_weight
                print(sum)
                print(my_stored_weight)

            
        weighted_avg = sum / my_stored_weight
        print(f"The current average for the student is... {weighted_avg}%")
    
        return weighted_avg
    
class  Homework(Assignment):
    pass

class  Quiz(Assignment):
    pass

class  Test(Assignment):
    pass





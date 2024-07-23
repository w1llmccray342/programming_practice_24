import calculate_avg

my_quiz_obj = calculate_avg.Assignment("Assignment", 0.1, 10)
my_hw_obj = calculate_avg.Homework("Homework", 0.2, 10)
my_test_obj = calculate_avg.Quiz("Quiz", 0.3, 10)
my_assign_obj = calculate_avg.Test("Test", 0.4, 10)

print(my_assign_obj, "\n", my_test_obj, "\n", my_hw_obj, "\n", my_quiz_obj)

# Create a master list to store objects created for quiz, hw, test, assign TYPE ASSIGNMENT objects
my_quiz_objs = []
my_assign_objs = []
my_test_objs = []
my_hw_objs = []
my_master_obj_list = [my_assign_objs, my_hw_objs, my_quiz_objs, my_test_objs]
my_master_class_list = [calculate_avg.Assignment, calculate_avg.Homework, calculate_avg.Quiz, calculate_avg.Test]
nums = 0
# Gather input from the user:

# 
for assignment_type in my_master_obj_list:
    nums_to_add = int(input(f"Please type the number of assignments you would like to check: \n"))

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

    for i in range(nums_to_add):
        my_score = float(input(f"Please enter the score for {my_name} #{i+1}"))
        my_obj_to_add = my_master_class_list[nums](my_name, my_weight, my_score)
    nums += 1

    
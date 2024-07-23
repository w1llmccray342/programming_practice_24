import calculate_avg

def display_master_list(obj_list):
    i = 1
    for object_type in obj_list:
        for object in object_type:
            print(f"OBJ#{i} of type {object}")
            i += 1

# Create a test object for my_master_list
my_class = calculate_avg.Assignment("Test", "Example", "NIL")

my_master_list = calculate_avg.Assignment.generate_master_list(my_class)
display_master_list(my_master_list)
calculate_avg.Assignment.calculate_average(my_master_list)


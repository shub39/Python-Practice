# Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# Given Function
def display_student(name, age):
    print(name, age)

def show_student(name, age):
    display_student(name, age)

show_student("Harold", 28)

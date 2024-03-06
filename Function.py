# pass by value function
name = "Zunaira"
id='01'
def my_func(name, id):
    return
print(name + id)

# function with default argument
def show_employee(name, salary=10000):
    print("Name:", name, "salary:", salary)
show_employee("Zunaira Hameed", 12000)
show_employee("Zunaira Mughal")

# pass by variable
def modify_string(s):
    print("Inside modify_string, before modification, s =", s)
    s = s + " World!"
    print("Inside modify_string, after modification, s =", s)
def main():
    my_string = "Hello"
    print("Before calling modify_string, my_string =", my_string)
    modify_string(my_string)
    print("After calling modify_string, my_string =", my_string)

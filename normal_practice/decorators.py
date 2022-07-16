

def greeting(func):
    def add_greeting(name):
        return "Hi " + func(name) + ',\n' + "You will do you best " + func(name)

    return add_greeting


@greeting
def my_name(name):
    return name

name = str(input("Please enter your name: "))
print(my_name(name))

"""‘add()’ returns sum of x and y passed as arguments but it is wrapped by a decorator function, 
calling add(2, 3) would simply give sum of two numbers but when we call add.
data then ‘add’ function is passed into then decorator function ‘attach_data’ as argument and 
this function returns ‘add’ function with an attribute ‘data’ that is set to 3 and hence prints it.

Python decorators are a powerful tool to remove redundancy.
"""

def argument_return(func):
    func.data = 7
    return func

@argument_return
def add_values(a, b):
    return a + b

print('111: ', add_values(5, 6))
print('222: ', add_values.data)
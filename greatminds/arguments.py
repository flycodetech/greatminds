

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("welcome onboard") 


greet("success", "Nwankwo")
#the paramitters take input for your argument      while argument is the actual paramitter
#types of functions 

#in programming we have two types of functions 
# 1- function that perform a task eg the code above 
# 2- function that returns a value eg  round(1.0)

def greet(name):
    print(f"hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("james") 
file = open("content.txt", "w")
file.write(message)
print(message)

def increment(number, by):
    return number + by

print(increment(2, 1))

    #we can put it this way print(increment(2, by=1))

    #back to iteration 

def multiply(*numbers):
    total = 1
    for number in numbers: 
        total *= number 
    return total


print(multiply(2, 3, 4, 5))

def greeting(args):
 

 greeting()

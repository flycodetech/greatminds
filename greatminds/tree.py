import math
import calendar

import money 


#def create_christmas_tree(height):
    #for i in range(height):
       #print(' ' *(height - i - 1 ) + "*" *(2 * i + 1 )) # type: ignore
       #print(' ' * (height - 1)+ '|') # type: ignore
#height = int(input("enter the height of the christmas tree: "))
#create_christmas_tree(height) # type: ignore

#my_str = "hello john i am to be the teacher 30"
#reversed_str = my_str[: :-1]
#print(reversed_str)


#code = "we are not in Nigeria at the moment"
#reversed_str = code[: :-1]
#print(reversed_str)
#print()

school = "nesgel, westbay, zineth "
reversed_string = school[: :-4]
reversed_string = school[: :-1]
reversed = school[: :-2]
print(reversed_string)



#length

course = "   Python \n Programming "
print(course)


first = "success"
last = "Nwankwo"

full = f"{last} {first}"

print(full)

print(course.strip())

#strip to remove white spaces 
#rstrip lstrip
#to find the indext of a character we use .find("pro")
#replace use to replace characters 
dance = "waka  maka"
print(dance)
print(dance.replace("b", "e"))
#to check for an existing character 
print("wed" in dance)
print("wed" not in dance)

# in python we have 3 types of number 
#integer 
#float 
#complex e.g a + bi
x =  1 + 2j #complex number 
#if you want a single number from use (// not /)
#operators are (*, -, +, /, //, % mojulars, **)

#assignment operator 
x = 10
x = x + 3
x =+ 3
print(x)
# working with numbers 
print(round(3.8))
# we have another useful one called abs
print(abs(-3.8))
# if you want to write a complex mathematical problem 
# that involves numbers you need to use the mathematical module 
# we need to import the module to use it  

print(math.ceil(2.2))

#type coversion
x = input("x:")
y = int(x) + 1
print(f"X: {x}, y:{y}")

#comparison operations 
#greather and lessthan signs 
#ord
#condtional statements 

temperature = 15

if temperature > 30:
    print("its warm")
    print("Drink water")
elif temperature > 20:
    print("its a lovely day ")
else:
    print("its cold")
print("Done") 

age = int(input("input your age "))
if age >= 18:
    message = "Eligible"
else: 
    message = "not Eligible"
print(message)

high_income = False
good_credit = True
student = False 

if high_income and good_credit and not student:
    print("Eligible")
else: 
    print("not Eligible")

#chaining comparison operators 
age = 22
#if age >= 18 and age < 65:
    #or
if 18 <= age < 65:
    print("Eligible")

#for loop

for number in range(1, 10, 2):
    print("attempt", number , number * ".")


cal = calendar.month(2026, 3)
print("Here is the calendar:")
print(cal)

import time;
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

print("time.altzone %d " % time.altzone)

#functions 

# Function definition is here
def printme( str ):
 "This prints a passed string into this function"
 print(str)
 return
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def changeme( mylist ):
 "This changes a passed list into this function"
 mylist.append([1,2,3,4])
 print("Values inside the function: ", mylist)
 return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print("Values outside the function: ", mylist)


print("i am coming from, {money}")






























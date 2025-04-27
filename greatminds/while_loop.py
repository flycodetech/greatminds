successful = False
for number in range(3):
    print("Attempt")
    if successful: 
        print("successful")
        break
else:
    print("attempted three times  and failed ")

    #nesting loop 

    #for x in range (5):
        #for y in range(3):
         #   for z in range(5):
         #     print(f"{x}, {y}, {z}")
#itrations 
#print(type(5))
#print(type(range(5)))

#what is good about this range function is that it is iterable
#that why you can write a xcode that looks like this , 
#for x in range(5):
    # strings are also iterable 
#examples for strings

for x in "python":
    print(x)

    for y in [1, 2, 3, 4]:
        print(y)
     

print(f"{x}, {y}")

#while_loop
#example 

number = 100
while number > 0:
     print(number)
     number //= 2
#another examples of while loop

command = " "
while command.lower() != "quit"   !="QUIT":
    command = input(">")
    print("ECHO", command)
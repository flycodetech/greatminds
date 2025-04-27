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

#reversed iteration 4 ways 

#using function 

fruits = ['apple', 'banana ', 'cherry']

#for fruits in reversed(fruits):
     #print(fruits)

#using using  slicing with a step of -1
 
#for fruit in fruits [: :-1]:
    #print(fruits)

#using function  with a nagative step 
#for i in range(len(fruits)-1, -1, -1):
    #print(fruits[i])

#using while loop

#i = len(fruits) - 1

#while i >= 0: 
      #print(fruits[i]) 
      #i -=1

#for single string 
#1- using slicing 

s = "success"

#reversed_s = s[: :-1 ]
#print(reversed_s)

#2- using  reversed function 

#reversed_s = " ".join(reversed(s))
#print(reversed_s)

#3- using loop
#reversed_s = ""
#for char in s:
    #reversed_s = char + reversed_s 
    #print(reversed_s)

#4- using recursion 
#def reverse_string(s):
    #if len(s) == 0:
       # return s
    #else:
        #return
    #reverse_string(s[1 :])+ s[0]
    #s = "success"
    #reverse_string = reverse_string(s)
    #print(reverse_s)

#while True:
 #       coffee = 'coffee situation '
  #      if coffee == 'empty':
     #       print('fill')
      #      break
       # elif coffee =='full':
        #    print('drink')
         #   break
       # else:
        #    print('it\'s okey')
         #   pass
          #  print('so  proceed ..........') 
           # break

#for loop = excute a brock of code a fixed number of times. you can iterate over a range, string, sequence etc. 

for x in range(1, 21 ):
    if x == 13:
        continue
    else: 
        print(x)

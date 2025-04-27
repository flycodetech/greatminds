#nested loop = A loop withing another loop(outer, inner)
 #outer loop:
     #inner loop
#you could have another strutured withing nother loop
#you could hve  while loop inside  forloop nd  forloop inside a whi;e loop 

#smple
# while X > 0:
#     while y > 0:
#         print('do something ')

# while X > 0:
#     for y in rnge(9):
#         print('do something ')


# for X > 0:
#     for y in rnge(9):
#         print('do something ')

for x in range(1, 10):
    print(x) # we can add  (x, end="") to make them be on the same line 
# to mke it repeat four time . 
for x in range(3):
    for y in range(1, 10):
      print(y, end=" ")
#to make it print on  new line we add another printline 
    print()
   
#create a rectangle 
#project
rows = int(input("enter the # of rows: "))
columms = int(input("enter the # of columms: "))
symbol = input('Enter  symbols to use ')

for x in range(rows):
    for y in range(columms):
      print(symbol, end="")  
    print()



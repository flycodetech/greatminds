#for loops = excute a block of code a fixed number of time 
#you can iterate over a range, string, sequence, etc. 

for x in  range(1, 11):
     print(x)
#to count backwords you can use the reverse function 
for x in  reversed(range(1, 11)):
    print(x)

print('happy new year ')

#you can count by any number by including the step 
for x in  range(1, 11, 2):
    print(x)

#you can iterate over a number 
credit_card = "2134-5678-9034-4356"

for x in  credit_card:
    print(x)

#to continue counting 
for j in  range(1, 21):
    if j == 13:
       continue

else:
    print(j)
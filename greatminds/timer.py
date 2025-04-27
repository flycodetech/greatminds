import time 

my_time = int(input("enter the time in seconds:  "))

for x in reversed(range(0, my_time )): #we can also use a step 
    #which can be done by (my_time,  0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 365)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(3)


print("Time's Up!")
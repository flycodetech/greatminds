from dataclasses import astuple


def printme( str ):
 "This prints a passed string into this function"
 print(str)
 return
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")



greets = input('input your nme ')

def greet(greets):
    
 
 print(greets)

 

 return

greet(f'good moring mr {greets} its 7m ')
greet(f'whts you pln for tody {greets}? ')
greet(f'would you like tie {greets}?')




def changeme( mylist ):
 "This changes a passed list into this function"
 mylist.append([1,2,3,4])
 print("Values inside the function: ", mylist)
 return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


 
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print( "Output is: ") 
    print(arg1)
    for var in vartuple:
        print(var)
    return
    # Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
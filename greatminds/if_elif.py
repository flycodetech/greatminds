#if = do some code only if some condition is true 
# else do something else 

age = int(input('enter your age:  '))

if age >= 100:
    print('you are too old to sign up')
elif age >= 18:
    print('you are now signed up!')

elif age < 11:
    print('you are still very young to sign up ')
else:
    print('you must be 18+ to sign  up ')


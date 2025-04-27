#logical operators  = evaluate multiple condition(or, and , not)
#                or = at least one condition  must be True 
#                and = both conditons must be true 
#                not = inverts the condition (not false, not true )

from tokenize import Funny


temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print('the outdoor event is cancelled ')
else:
    print('The outdoor event is still scheduled ')


temp = 28
is_sunny = False

if is_sunny >= 28 and is_sunny:
    print('it is Hot outside ')
    print('it is sunny')
elif temp <= 0 and is_sunny:
    print('it is cold outside ')
    print('it is sunny')
elif 28 > temp > 0 and is_sunny:
    print('it is warm outside ')
    print('it is sunny')
elif is_sunny >= 28 and not is_sunny:
    print('it is Hot outside ')
    print('it is cloudy')
elif temp <= 0 and not is_sunny:
    print('it is cold outside ')
    print('it is cloudy')
elif 28 > temp > 0 and not is_sunny:
    print('it is warm outside ')
    print('it is cloudy')

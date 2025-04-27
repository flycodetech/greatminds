weight = float(input('enter your weight: '))
unit = input('kilograms or pounds? (k or l): ')

if unit == 'k':
    weight = weight * 2.205
    unit ='lbs.'
    print(f'your weight is :{unit} {unit}' ) 
elif unit == 'L':
    weight = weight / 2.205
    unit = 'kgs.'
    print(f'your weight is :{unit} {unit}' ) 
else: 
    print(f'{unit} was not  valid ' )


    
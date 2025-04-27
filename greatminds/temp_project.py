unit = input('Is this tempurature in celsius or fehrenheit(C/F):  ')
temp = float(input('enter the tempurature: '))

if  unit == 'C':
    temp =  round((9 * temp) / 5 + 32,  1)
    print(f'The tempurature in Fehrenheit is: {temp} of')
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The tempurature in celsuis is: {temp} oC')
else:
    print(f'{unit} is an invalid unit of measurement')
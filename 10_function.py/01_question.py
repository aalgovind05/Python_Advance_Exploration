name = input('tell me your name :')
pin = int(input('tell me your password :'))

if name == 'govind' and pin == 1234:
    print('welcome sir')
elif name != 'govind'and pin == 1234:
    print('tumse na ho payega beta')
elif name == 'govind' and pin != 1234:
    print('sale chor')
elif name != 'govind' and pin != 1234:
    print('kal aana beta')
    
a = int(input('give me 1st num: '))
b = int(input('give me 2rd num: '))
c = int(input('give me 3rd num: '))

if a<b and a<c:
    print('a is a smallest number:', a)
elif b<c:
    print('small is: ',b)
else:
    print('smallest is: ',c)
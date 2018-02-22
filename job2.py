import random


aa = random.randint(1,10)

print aa

bb = ''

while bb is not int:
    try:
        bb = int(input("i need a number: "))
        break
    except NameError:
        print('please enter a valid number,')
    except SyntaxError:
        print('please enter a number,')
print bb

while (bb != aa):
        bb = input('guess a number again: ')

print "correct"

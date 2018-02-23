import random


aa = random.randint(1,10)

print ("the random number is " + str(aa))

#bb = ''

#while bb is not int:
 #   try:
 #     bb = int(input("i need a number: "))
  #      break
  #  except ValueError:
  #      print('please enter a valid number,')

#print (bb)
#bb = int(input("i need a number: "))
#print (bb)
bb = ''
while (bb != aa):
#        bb = int(input('guess a number again: '))
	while bb is not int:
		try:
			bb = int(input("i need a number: "))
			break
		except ValueError:
			print('please enter a valid number,')
	print (bb)
print ("correct")

import random
import query
import sys

while True:
	try:
		number = int(input('Choose a number between 0 and 10:'))
	except ValueError:
		print("That is not a number.")
		continue
	if number > 10:
		print('Your number is too large.')
		continue
	elif number < 0:
		print('Your number is too small.')
		continue
	break

result = random.randint(0, 10)

print("You're number: " + str(number))
print("Our number: " + str(result))

if number == result:
	print('Congratulations!')
else:
	print('Close, but no cigar.')

while True:
	try:
		answer = query.query_yes_no('Do you wish to contunue?')
		if answer == "yes":
			while True:
				try:
					number = int(input('Choose a number between 0 and 10:'))
				except ValueError:
					print("That is not a number.")
					continue
				if number > 10:
					print('Your number is too large.')
					continue
				elif number < 0:
					print('Your number is too small.')
					continue
				break
			result = random.randint(0, 10)
			print("You're number: " + str(number))
			print("Our number: " + str(result))
			if number == result:
				print('Congratulations!')
				continue
			else:
				print('Close, but no cigar.')
				continue
		elif answer == "no":
			print('Goodbye.')
			break
	except:
		pass

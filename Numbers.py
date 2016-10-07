import random
import query
import sys

while True:
    try:
        number = int(input('Choose a number between 0 and 10:'))
        break
    except ValueError:
        print("That is not a number.")
result = random.randrange(10)
while number > 10:
    print('Your number is too large.')
    number = int(input('Choose a number between 0 and 10:'))
print(result)
if number == result:
    print('Congratulations!')
else:
    print('Close, but no cigar.')
answer = query.query_yes_no('Do you wish to contunue?')
while answer == "yes":
    while True:
        try:
            number = int(input('Choose a number between 0 and 10:'))
            break
        except ValueError:
            print("That is not a number.")
    result = random.randrange(10)
    while number > 10:
        print('Your number is too large.')
        number = int(input('Choose a number between 0 and 10:'))
    print(result)
    if number == result:
        print('Congratulations!')
    else:
        print('Close, but no cigar.')
    answer = query.query_yes_no('Do you wish to contunue?')
if answer == "no":
    print('Goodbye.')

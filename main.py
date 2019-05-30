# def div42by(divby):
# 	try:
# 		return 42/divby
# 	except ZeroDivisionError:
# 		print("Error: You tried to divide by zero.")


# print(div42by(45))
# print(div42by(42))
# print(div42by(0))

# while True:
# 	num=input("Enter a number\n")
# 	try:
# 		if int(num)%2==0:
# 			print("Number is even")
# 		else:
# 			print("Number is odd")
# 		break
# 	except:
# 		print("Please enter valid data!")


import random
import sys

print("Hello, What is your name?")
name = input()
print("Well, " + name + ", I am thinking of a number between 1 and 20.\n")
secretNumber = random.randint(1,20)


try:
	for guessessTaken in range(1, 7):
		guess1  = int(input("Take a guess\n"))
		if guess1 < secretNumber:
			print("Your guess is less than secretNumber ")
		elif guess1 > secretNumber:
			print("Your guess is higher than secretNumber")
		else:
			break
except:
	print("Value is not valid")



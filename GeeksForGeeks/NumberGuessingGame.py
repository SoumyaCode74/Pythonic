from random import randint

start = int (input ("Enter the start value: "))
end = int (input ("Enter the last value: "))
actual = randint (start, end)


# This algorithm of guessing by finding half of a range is same as Bisection method of approximating
# a root of an equation between a given range
def min_guesses (actual, start, end, count = 1):
	guess = (start + end) // 2
	if guess == actual:
		i = 1
		while True:
			guess = int (input ("Guess: "))
			if i > count:
				print (f"Better Luck Next Time! The actual number was: {actual}")
				break
			if guess == actual:
				print ("Congratulations! ")
				break
			elif guess < actual:
				print (f"Try Again! You guessed too small: {guess}")
				i += 1
			else:
				print (f"Try Again! You guessed too high: {guess}")
				i += 1

	elif guess < actual:
		count += 1
		min_guesses (actual, start = guess, end = end, count = count)
	else:
		count += 1
		min_guesses (actual, start = start, end = guess, count = count)


min_guesses (actual, start, end)

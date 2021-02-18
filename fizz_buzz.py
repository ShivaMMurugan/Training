def fizzbuzz(n):
	for number in range(1, n):
		
		if number % 3 == 0 and number %5 == 0:
			print("FizzBuzz")
		elif number % 3 == 0:
			print("Fizz")
		elif number % 5 == 0:
			print("Buzz")
		else:
			print(number)

fizzbuzz(51)



# Task


def combo(k, v):
...     combinations = []
...     for i in k:
...             for j in v:
...                     combinations.append([i, j])
...     return combinations
... 
>>> combo(["vanniala", "chocolate"], ["chocolate_sauce"])
[['vanniala', 'chocolate_sauce'], ['chocolate', 'chocolate_sauce']]
>>> 


# two parameters
input
["vanniala", "chocolate"], ["chocolate_sauce"]

output
[["vanniala", "chocolate_sauce"], ["chocolate", "chocolate_sauce"]]
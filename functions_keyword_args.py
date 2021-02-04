def add_value(a=10, b=20): # keyword arguments in function
	print(a , b)
add_value()

def star_args(*args):
	print(*args)
	# print(*kwargs)
star_args(100, 200, 300, 400, 500)

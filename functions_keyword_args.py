# #type 1

# def say_hello():
# 	print("Hello world")
# say_hello()


# # type 2

# def add(a, b):
# 	print(a + b)
# add(10, 20)

# # type3

# def add_value(a=10, b=20): # keyword arguments in function
# 	print(a , b)
# add_value()

# # type4
# def star_args(*args):
# 	print(*args)
# 	# print(*kwargs)
# star_args(100, 200, 300, 400, 500)

def add_list(l):
	empty_list = []
	for i in l:
		empty_list.append(i)
	return empty_list
print(add_list([10, 20, 30, 40, 50]))




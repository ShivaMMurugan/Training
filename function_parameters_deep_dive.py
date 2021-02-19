#regular function
def myfunc():
	print("normal function")

myfunc()

# parameter based functions

def get_params(p1, p2):
	print(p1 * p2)

get_params(10, 10)


# *args


def im_special(*args):
	print(args)

im_special(10, 10, 10, 10, 10)


# keyword only argument

def im_also_special(b, a=100, c=100):
	print(b, a * c)

im_also_special(136)

# **kwargs

def names(*args, **kwargs):
	print(args)
	print(kwargs)

names(10, 10, "python", myname="shiva", college="dgvc")



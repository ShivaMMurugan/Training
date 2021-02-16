def addition(a, b, c):
	print(a + b + c)

addition(10, 20, 1)

x = lambda a, b, c: a *b * c

print(x(10, 20, 25))


s = lambda sample, sample2: sample[::-1] + sample2

print(s("python", "flhdviutg uoiwd"))
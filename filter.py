def filter_me(param1):
	if param1 < 18:
		return False
	else:
		return True

ages = [8, 7, 13, 18, 32, 44]

# conv = filter(filter_me, ages)

# print(list(conv))


lambda_implementation = lambda val: True if val >= 18 else False

d = filter(lambda_implementation, ages)
print(list(d))


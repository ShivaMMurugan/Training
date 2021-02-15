elements = ['abs', 'core', 'delta', 'compliance', 'aws']

for city in elements:
	if city == "delta":
		print("Found city named {}".format(city))
		break # breaks completly
	else:
		print(city)


for city in elements:
	if city == "delta":
		print("Found city named {}".format(city))
		continue #skip
	else:
		print(city)


n = 1

while n < 10:
	print("Printing {}".format(n))
	n += 1
l1 = {"farm", "garden", "flowers", "extra"}
l2 = ["farmer", "gardner", "random"]

d = dict()
# break the loop when a shortest iterable is exhausted.
for data, value in zip(l1, l2):
	d[data] = value
print(d)

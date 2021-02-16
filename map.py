def aflhdflj(l):
	return len(l)
# print(aflhdflj(["apple", "orange"]))

mapper = map(aflhdflj, ["apple", "orange", "dates"])
print(list(mapper))

# 1. Any function name
# 2. Iterable (str, list, tuple, dict, set)
names = ["Arvind", "Bala", "Shiva", "Dinesh"] # Mutable

#Indexing []
# print(names[0]) #valid
# print(names[4]) #IndexError: Index out of range

# Mutable
# print("Im printing from line number 8 of list {}".format(names))
# names[0] = "Ganesh"
# print(f"Im printing from line number 10 of list {names}")

# list methods

# 1 upper only for strings

# print(names.upper()) 
# AttributeError: list object has no attribute upper

# 1 append()

# name = "Ganesh"

# names.append(name)
# print(names)

# 2 Extend method

# l = ["Ganesh", "Barath", "Surya"]
# names.extend(l)
# print(names)

# 3 pop
  # * removes the last element by default
  # * can pass an index value to remove the particular field
# names.pop()
# print(names)
# print(dir(names))
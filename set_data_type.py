names1 = {"Ajith", "Arjun", "David", "Surya"}
names2 = {"Ajith", "Arjun", "David", "Surya", "Bala"}
# print(names)
# print(type(names))
# print(dir(names))

#Indexing

# print(names[0]) not possible

# @order not maintained

#item assignment not possible

# names[0] ="Ninja"

# @set difference

# diff = names2.difference(names2)
# diff = names2 - names2
# print(diff)

#intersection

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2 = [1, 2, 3, 4, 5, 22, 65, 99, 88]

# diff = set(l2).intersection(l1)
# print(diff)

#update
#updates the existing set. 
# Same elements will be ignored if present already.
names1.update(names2)

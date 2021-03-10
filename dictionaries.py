d = {"name": "Surya", "age": 22, "college": "some college"}
#Keys are immutable, values can be changed.
# print(d)
# print(dir(d))
#Access values based on key
# 1 []
# get


# print(d["name"])
# print(d["names"]) #KeyError, when a key is not exists
# print(d.get("names", "Key not found"))

#only keys

# print(d.keys())

#only values
# print(d.values())

# #items
# print(d.items())

#update a dictionary
# d.update(name="Dhanush", age=20, college="Dgvc", dept="cs")
# print(d)

# pop
# d.pop("name")
# print(d)

# del d["name"]
# print(d)
# print(dir(d))

# k = ["name", "age", "college"]
# if k[0] in d:
#   d.update("college"="velammal", "age"=25, "name"="Muthu")
#   print(d)
#  else:
#   print("Invalid)

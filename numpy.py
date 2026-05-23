person2 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
def print_hello():
  print("hello world")








import json

my_set = list({42, "apple", 3.14, True})
my_tuple = ("banana", 99, 2.718, False)
my_dict = {
    "id": 101,
    "name": "Alice",
    "score": 88,
    "active": True
}
my_list = [7, "orange", 15.6, "apple", 7]

data = {
    "my_set": my_set,
    "my_tuple": my_tuple,
    "my_dict": my_dict,
    "my_list" : my_list,
}
with open("my.json", "w") as f:
    json.dump(data, f, indent= 3)

with open("my.json") as f:
  print(json.load(f))
list1 = list(("apple","apple", "banana", "cherry", "pear", "kiwi", "melon", "grapes", "peach", "apricot"))
tuple1 = tuple(list1)
print(tuple1)
t = "orange",
tuple1 += t
print("orange" in tuple1)
for x in range(len(tuple1)):
    print(tuple1[x])


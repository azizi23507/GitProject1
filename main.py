"""list1 = list(("apple","apple", "banana", "cherry", "pear", "kiwi", "melon", "grapes", "peach", "apricot"))
print("apple" in list1)
list2 = [x.upper() for x in list1]
print(list2)

newList = ["even" if x % 2 ==0  else "odd" for x in range(10)]
print(newList  )

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
tuple1 = tuple(list1)
print(tuple1)
t = "orange",
tuple1 += t
print("orange" in tuple1)
for x in range(len(tuple1)):
    print(tuple1[x])

myset = {"apple", "banana", "cherry"}
print(myset)
for x in myset:
    print(x)
print("banaNA".lower() in myset)

thisDict = {"Name": "Shabir", "email": "shabir@gmail.com", "age": "28", "gender": "male"}
thisDict["Name"] = "Basir"
thisDict.update({"age": "32"})
thisDict.popitem()
print(thisDict)
print(thisDict["Name"])
print(thisDict.get("Name"))
print(thisDict.keys())
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
print(thisDict.values())

for x, y in thisDict.items():
    print(x, y)"""

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Linus",
        "year": 2011
    }
}

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

for x, obj in myfamily.items():
    print(x)

    for y, z in obj.items():
        print(y + ':', z)
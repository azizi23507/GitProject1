
"""class Test:
    def __init__(self, name = None, age = None, test_result = False): # the first parameter is always self, which represents the object's instance in which we can call the attribute

        self.name = name
        self.age = age
        self.test_result = test_result

    def __str__(self):
        return f"this is the name {self.name}, and this is the age {self.age} and this is the result {self.test_result}"

    def print_name(self):
        print(f"the person's name is {self.name}")
    def print_age(self):
        print(f"the person's age is {self.age}")
    def print_test_result(self):
        if self.test_result is True:
            print("the person passed the exam")
        else:
            print("the person failed the exam")



t1 = Test("shabir", "2", True)
print(t1)
t1.print_name()
t1.print_age()
t1.print_test_result()




class Person:
    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def print_name(self):
        print(f"this the first name of the person {self.firstname},"
              f" and this is the last name of the person {self.lastname}")


class Student(Person):
    def __init__(self, firstname=None, lastname=None, score=None, result=None):
        super().__init__(firstname, lastname)
        self.score = score
        self.result = result

    def __str__(self):
        return (f"my name is {self.firstname}, my last name is {self.lastname}"
                f" my grad is {self.score}, and my result is {self.result} ")

p1 = Person("shabir", "basir")
print(p1)

s1 = Student("Tom", "Muller", 75, "Passed")
print(s1)


mystr = "banana"
myit = iter(mystr)

print(myit)



class MyNumber:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current


mynum = MyNumber(1,7)
for i in mynum:
    print(i)


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()






"""
import json
"""
list1 = list(("apple","apple", "banana", "cherry", "pear", "kiwi", "melon", "grapes", "peach", "apricot"))
print("apple" in list1)
list2 = [x.upper() for x in list1]
print(list2)

newList = ["even" if x % 2 == 0  else "odd" for x in range(10)]
print(newList)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)
print(thislist)


tuple1 = tuple(list1)
print(tuple1)
t = "orange",  # is another tuple
tuple1 += t    # adding a tuple to another tuple
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
print(thisDict.values())

for x, y in thisDict.items():
    print(x, y)

my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Linus",
        "year": 2011
    },
    "child3": {"name": "Tobias",
        "year": 2007
}}

for x, obj in my_family.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

for x, obj in my_family.items():
    print(x)

    for y, z in obj.items():
        print(y + ':', z)
a = 2
b = 2
#print("a") if a > b else print("b") if a < b else print("=")




list1 = [x for x in range(1, 21) if x % 2 == 0 ]
words = ["apple", "banana", "cherry", "date"]
list2 = [len(x) for x in words]
list3 = [x**2 for x in range(1, 11) if (x ** 2) % 4 == 0]
list4 = [(x, y) for x in range(1, 4) for y in range(1, 3) if (x + y) % 2 == 0]
#new_list = [x if x != "banana" else "orange" for x in fruits] 

print(list4)


import re # regular expression
txt = "the eerie tree Seemed freed from three green weeds"
x = re.search("eer", txt) # search for the first occurrence of the pattern "eer" in the string txt and return a Match Object.
print(x.group()) # If there is no match, the value None will be returned, instead of the Match Object.

if x:
    print(True)
else:
    print(False)

y = re.findall("ree", txt)
print(y)

z = re.split("ee", txt, )
print(z)

a = re.sub("ee", "ff", txt)
print(a)


flag = True
while flag:
   try:
        customer_review = float(input("please enter your review: "))
        flag = False
   except ValueError:
        print("invalid character enter again")



if not ( 1<= customer_review <= 5):
    print("wrong rating")
elif customer_review >= 4.5:
    print("Extraordinary")
elif customer_review >= 4:
    print("Excellent")
elif customer_review >= 3:
    print("Good")
elif customer_review >= 2:
    print("Fair")
else:
    print("Poor")
    
    
import cowsay
cowsay.cow("Good Mooooorning!")


# convert form json to python
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["name"])

# convert from python to json
x = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "grade": True,
    "result": None,
}
y = json.dumps(x)
print(y)

# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

z = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(z, indent=4))

with open("text.txt", "a") as f: # append mode
    f.write("\nthe is the extra line of the text")

with open("text.txt", "r") as file: # read mode
    for x in file:
        print(x, end="")

import os
if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("the does not exist")

from test import print_hello as p
p()
import datetime

x = datetime.datetime.now()
print(x.strftime("%B %d/%b/%Y  %I:%M:%S %p"))



import json


with open("text.json", "r") as f:
    data = json.load(f)
users = {}
for x in range(len(data)):
    users[f"user {x + 1}"] = data[x]
print(users)
user_id = []
for ids, dicts in users.items():
    for keys, values in dicts.items():
        if keys == "user_id":
            user_id.append(values)

print(user_id)


from pathlib import Path

path = Path("text.txt")
contents = path.read_text().strip()
lines = contents.splitlines()

for x in lines:
    print(x)

    
print(type(lines))
listl = []
with open("text.txt", "r") as f:
    for x in f:
        listl.append(f.readline().strip())
print(listl)

print(json.dumps({"string"}))







import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()



class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"the name of the person is {self.__name} and the age of the person is {self.__age}"
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_age(self, age):
        self.__age = age
    def get_age(self, age):
        return self.__age
p2 = Person("ahmmad", 23)
print(p2)
p2.set_age(35)
print(p2)

import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shabir123",
    # database = "test"
)

# my_cursor.execute("CREATE DATABASE mydatabase")

my_cursor.execute("SHOW DATABASES")
databases = my_cursor.fetchall()
for database in databases:
    print(database)
my_cursor.execute("drop table customers")
my_cursor.execute("CREATE TABLE customers (id INT, name varchar(255), address varchar(255))")
my_cursor.execute("ALTER TABLE customers MODIFY column id INT NOT NULL AUTO_INCREMENT PRIMARY KEY")
my_cursor.execute("SHOW CREATE TABLE customers")
print(my_cursor.fetchall())



my_cursor.execute("USE mydatabase")
my_cursor.execute("SHOW TABLES")
tables = my_cursor.fetchall()
for table in tables:
    print(table)

my_cursor.execute("DELETE FROM customers where id = 2")
my_cursor.execute("INSERT INTO customers(name, address) VALUES ('aziz', 'Pfarrkirchen')")
mydb.commit()
my_cursor.execute("SELECT * FROM customers")
tables = my_cursor.fetchall()
for table in tables:
    print(table)


my_cursor = mydb.cursor()
my_cursor.execute("USE world")
my_cursor.execute("SELECT * FROM country")
items = my_cursor.fetchall()

first_row = [col[0] for col in my_cursor.description]
print(tabulate(items, headers=first_row, tablefmt="psql"))
print(my_cursor.description)

try:
    my_cursor = mydb.cursor()

    my_cursor.execute("SHOW DATABASES")
    database = my_cursor.fetchall()
    for database in database:
        print(database)
    print()
    print()
    my_cursor.execute("USE mydatabase")

    my_cursor.execute("SHOW TABLES")
    tables = my_cursor.fetchall()
    for table in tables:
        print(table)

    print()
    my_cursor.execute("SELECT * FROM customers")
    items = my_cursor.fetchall()
    for item in items:
        print(item)

    
    #sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    #val = ('mahmod', 'kabul')
    #my_cursor.execute(sql, val)
    #mydb.commit()
except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if mydb.is_connected():
        my_cursor.close()
        mydb.close()
        print("MySQL connection is closed")"""





x = [0] * 6
print(x)


















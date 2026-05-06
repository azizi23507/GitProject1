# Hash table (Hash set and hash map)
# time complexity of O(1)

# A Hash Table is a data structure designed to be fast to work with.
#
# The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching
# for, adding, and deleting data can be done really quickly, even for large amounts of data.
#The most important reason why Hash Tables are great for these things is
# that Hash Tables are very fast compared Arrays and Linked Lists, especially for large sets.
# what is a hash code?
#A number generated from the key by the hash function. It tells us which bucket to put the entry or the key in.

my_array = ["Pete", "Jones", "Lisa", "Bob", "Siri"]

my_hash_set = [[] for _ in range(11)]

# take an array as parameter and extracts each element from the array and insert in the hash set based on the sum of the
# unicod of the letters mod 10 which gives an index.
def hash_creating_function(array):
    if not isinstance(array, list):
        array = [array]
    for value in array:
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)
        index = sum_of_chars % 11
        # Since each element of the my_hash_set is another array so the index refer
        # to one array not one element and that's why the bucket becomes as array.
        bucket = my_hash_set[index]
        if value not in bucket:
            bucket.append(value)

hash_creating_function(my_array)
hash_creating_function("Tom")
hash_creating_function("Stuart")
print(my_hash_set)

def hash_function(value):
    return sum(ord(char) for char in value) % 10
def contains(name):
    index = hash_function(name)
    return my_hash_set[index] == [name]
print(contains('Bob'))
print()
print()

# hash set
# A Hash Set is a form of Hash Table data structure that usually holds a large number of elements.
# Hash Set = hash table of keys only (Every element is a unique key)
# Hash Set → stores only the element (hashed to find bucket).
# In hash set, the element itself is hashed to find its bucket.
class SimpleHashSet:
    def __init__(self, size = 100):
        self.size = size
        self.hash_set = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = hash_function(value)
        bucket = self.hash_set[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = hash_function(value)
        bucket = self.hash_set[index]
        return value in bucket

    def remove(self, value):
        index = hash_function(value)
        bucket = self.hash_set[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        print("Hash Set contents:")
        for index, bucket in enumerate(self.hash_set):
            print(f"Hash set {index}: {bucket}")

hash_set = SimpleHashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()
print(hash_set.hash_set)
print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))

print()
print()



# hash Map
# Every entry is a key-value-pair, with a key that is unique, and a value connected it.
# Hash Map is a form of Hash Table data structure that usually holds a large number of entries.
# Hash Map = hash table of keys + values ( Hash Map = hash table of keys + values)
# In hash map, the key is hashed to find the bucket, and the value is stored alongside it.
# Hash Map → stores a key–value pair, using the hashed key to find the bucket.
# Bucket 8: [("123-4567", {"name": "Charlotte", "birth": "01-01-2000"})]
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.hash_map = [[] for _ in range(size)] # A list of buckets, each is a list (to handle collisions)

    def hash_function(self, key):
        # Sum only the numerical values of the key, ignoring non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return  numeric_sum % 10 # Perform modulo 10 on the sum that is the number of buckets too.

    def put(self, key , value):
        # Add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.hash_map[index]
        for i , (k, v) in enumerate(bucket): #i → index inside the bucket, (k, v) → key and value of each pair
            if k == key:
                bucket[i] = (key, value) # Update existing key
                return
        bucket.append((key, value)) # Add new key-value pair if not found

    def get(self, key):
        # Retrieve a value by key
        index = self.hash_function(key)
        bucket = self.hash_map[index]
        for k,  v in bucket:
            if  k == key:
                return v
        return None # if key not found

    def remove(self, key):
        # remove a key-value pair
        index = self.hash_function(key)
        bucket = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
             if k == key:
                 del bucket[i] # remove the key-value pair
                 return

    def print_map(self):
        # Print all key-value pairs in the hash map
        print("hash map contents:")
        for index, bucket in enumerate(self.hash_map):
            print(f"Bucket {index}: {bucket}")

# Creating the Hash Map from the simulation
hash_map = HashMap(size=10)

# Adding some entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()


print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")

print("Name associated with '123-4570':", hash_map.get("123-4570"))























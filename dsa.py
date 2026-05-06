
def fibonacci(n):
    if n < 2:
        return n
    else:

        return fibonacci(n - 2) + fibonacci(n - 1)
#print(fibonacci(20)) # this number means the index of the fibonacci sequence

def find_min(alist):
    mini_val = alist[0]
    for y in my_array:
        if y < mini_val:
            mini_val = y
    return mini_val



#Selection sort: repeatedly finds the smallest value and moves it to the beginning of the array.
#time complexity O(n^2)
my_array = [5,4,3,2,1,6,7,5,78,89,4,3,2,1,1,3,4,56,3,4,65,65,6,6,6,46,346,4,6,34,34,6]
for i in range(0, len(my_array) - 1):
    for j in range(i, len(my_array)):
        if my_array[i] > my_array[j]:
            temp = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = temp


#selection sort
#time complexity O(n^2)
my_array1 = [5,4,3,2,1,6,7,5,78,89,4,3,2,1,1,3,4,56,3,4,65,65,6,6,6,46,346,4,6,34,34,6]
print("array before selection sort algorithm", my_array1)
for i in range(0, len(my_array1) - 1):
    min_index = i
    for j in range(i, len(my_array1)):
        if my_array1[min_index] > my_array1[j]:
            min_index = j
    temp = my_array1[i]
    my_array1[i] = my_array1[min_index]
    my_array1[min_index] = temp

print("array after selection sort algorithm", my_array1)
print()

#Bubble sort: repeatedly compares adjacent elements and pushes the larger values toward the end of the array.
#time complexity O(n^2)
arrayBubble = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print("array before the bubble sort algorithm", arrayBubble)
for i in range(len(arrayBubble) - 1):
    for j in range(len(arrayBubble) - i - 1):
        if arrayBubble[j] > arrayBubble[j + 1]:
            temp = arrayBubble[j]
            arrayBubble[j] = arrayBubble[j + 1]
            arrayBubble[j + 1] = temp

print("array after the bubble sort algorithm",arrayBubble)
print()

#Insertion sort: take one element from the array and insert it into its correct position in the already sorted part of the array.
#time complexity O(n^2)
my_insert_array = [5,4,3,2,1,6,7,5,78,89,4,3,2,1,1,3,4,56,3,4,65,65,6,6,6,46,346,4,6,34,34,6]
print("array before the insertion sort algorithm", my_insert_array)
for i in range(1, len(my_insert_array)):
    insert_index = i
    current_value = my_insert_array[i]
    for j in range(i -1, -1, -1):
        if my_insert_array[j] > current_value:
            my_insert_array[j + 1] = my_insert_array[j]
            insert_index = j
        else:
            break
    my_insert_array[insert_index] = current_value

print("array after the insertion sort algorithm", my_insert_array)
print()


# Quicksort: an efficient, recursive divide-and-conquer algorithm that partitions the array around a pivot element.
# time complexity  O(n log n)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

qs_array = [64, 34, 25, 12, 22, 11, 90, 5]
print("array before the quick sort algorithm", qs_array)
quicksort(qs_array)
print("array after the quick sort algorithm", qs_array)
print()


#  counting sort: counts the occurrences of each unique element and uses this information to place elements in their correct positions.
# complexity for Counting Sort is O(n+k).
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)

    count = [0] * (max_val + 1)
    for i in arr:
        count[i] += 1

    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr
count_arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print("array before the counting sort algorithm", count_arr)
print("array after the counting sort algorithm", counting_sort(count_arr))
print()


# Radix Sort: Radix sort sorts numbers by processing digits from least significant to most significant,
# placing elements into digit-based buckets at each step until the array is fully sorted.
#  the time complexity O(n⋅k)

rad_array = [33, 45, 40, 25, 17, 24]
print("array before the radix sort algorithm ", rad_array)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(rad_array)
exp = 1

while maxVal // exp > 0:
    while len(rad_array) > 0:
        val = rad_array.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)
    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            rad_array.append(val)
    exp *= 10

print("array after the radix sort algorithm", rad_array)
print()

#  merge sort: In merge sort, the array is repeatedly split into halves until subarrays of size one are reached, then these
#  subarrays are merged back together in sorted order until the full array is sorted.
# the time complexity for merge sort is O(n⋅log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return  result

merge_array = [5,3,7,6,12, 11]
print("array before merge algorithm " , merge_array)
print("array after merge algorithm", merge_sort(merge_array))
print()

# Linear Search
#time complexity is O(n)
print("linear search algorithm")
def linear_search(arr_linear, target_val):
    for i in range(len(arr_linear)):
        if arr[i] == target_val:
            return i

    return -1

arr = [2,3,4,5,56,67,7,8,9,9,9,8,7,9,4,3,3]
print("the array for linear search algorithm is", arr)
target = 5
res = linear_search(arr, target)

if res != -1:
    print("value", target, "found at index", res)
else:
    print("value", target, "not found")

print()


# binary search
# time complexity is O(log n)
def binary_search(binary_array, target_val):
    left = 0
    right = len(binary_array) - 1

    while left <= right:
        mid = (left + right) // 2
        if binary_array[mid] == target_val:
            return mid
        if binary_array[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

bi_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
bi_target = 11

bi_result = binary_search(bi_array, bi_target)

print("the array for binary search algorithm is ", bi_array)
if bi_result != -1:
    print("value", bi_target, "found at index", bi_result)
else:
    print("target not found in array.")
print()


# A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer.
# The way they are linked together is that each node points to where in the memory the next node is placed.

# Double Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node1.prev = node4
node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.prev = node3
node4.next = node1

print("traversing forward: ", end="")
current_node = node1
start_node = node1
print(current_node.data, end=" -> ")
current_node = current_node.next
while current_node != start_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("...")

print("traversing backward: ", end="")
current_node = node4
end_node = node4
print(current_node.data, end=" -> ")
current_node = current_node.prev
while current_node !=end_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.prev
print("...")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def travers_print(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")

def min_value(head):
    minimum = head.data
    while head:
        if head.data < minimum:
            minimum = head.data
        head = head.next
    return minimum

def delete_node(head, target_node):
    if head == target_node:     #It deletes the first node by returning the second node as the new head of the list.
        return head.next

    current_node = head
    while current_node.next and current_node.next != target_node:
        current_node = current_node.next

    if current_node.next is None: # It prevents errors and handles the case where the node to delete doesn’t exist. The list stays the same.
        return head

    current_node.next = current_node.next.next

    # We return head so the list’s starting reference stays correct — especially if the first node was removed.
    return head

def insert_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node
    current_node = head
    for _ in range(position - 2):
        if current_node is None:
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    return head

node1 = Node(3)
node2 = Node(2)
node3 = Node(4)
node4 = Node(34)

node1.next = node2
node2.next = node3
node3.next = node4

#node1 = delete_node(node1, node2)
newNode = Node(43)
node1 = insert_node(node1, newNode, 3)
travers_print(node1)
print()
print()
#print("the minimum value of the the linked list is ", min_value(node1))






#stuck: LIFO (Last In First Out)

# stuck using array (list)
print("Stack for array (list)")
class Stack1:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


my_stack = Stack1()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print("stack: ", my_stack.stack)
print("Peek: ", my_stack.peek())
print("Pop: ", my_stack.pop())
print(my_stack.stack)
print("Peek ", my_stack.peek())
print("isEmpty:, ", my_stack.is_empty())
print("Size: ", my_stack.size())
print()
print()


# stuck using linked list
class Node1:
    def __init__(self, value):
        self.value = value
        self.next = None

print("Stack for linked list")
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node1(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("null")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.value

    def is_empty(self):
        return self.size == 0

    def stack_size(self):
        return self.size


my_stack2 = Stack()

my_stack2.push('A')
my_stack2.push('B')
my_stack2.push('C')


my_stack2.traverse()
print("Peak:, ", my_stack2.peek())
print("Pop: ", my_stack2.pop())
my_stack2.traverse()

print("Peek: ", my_stack2.peek())
print("isEmpty: ", my_stack2.is_empty())
print("Siz: ", my_stack2.stack_size())
print()


# queue: FIFO (First In Fist Out)
# queue using array (list)
queue = []

#Engueue
queue.append('A')
queue.append('B')
queue.append('C')


print("this is queue for array")
print(queue)
#Dequeue
element = queue.pop(0)
print("Dequeue: ", element)
print(queue)
#peak
front_element = queue[0]
print("Peek, ", front_element)

#isEmpty
is_empty = not bool(queue)
print("isEmtpy: ", is_empty)

# Size
print("Size: ", len(queue))
print("using class array for queue")

# queue using array (class)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# create the queue
my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print("Queue: ", my_queue.queue)
print("Dequeue: ", my_queue.dequeue())
print("Peek: ", my_queue.peek())
print("isEmpty: ", my_queue.is_empty())
print("Size: ", my_queue.size())


print("Queue using the linked list")

# queue using linked list
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue1:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1


    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def print_queue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# create a queue
my_queue1 = Queue1()

my_queue1.enqueue('A')
my_queue1.enqueue('B')
my_queue1.enqueue('C')

print("Queue: ", end="")
my_queue1.print_queue()

print("Dequeue: ", my_queue1.dequeue())
print("Queue: ", end="")
my_queue1.print_queue()
print("Peek: ", my_queue1.peek())
print("isEmpty: ", my_queue1.is_empty())
print("Size: ", my_queue1.size())






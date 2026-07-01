"""
Day 1 - Python Practice
Topics Covered:
1. Lists
2. Tuples
3. Dictionaries
4. Strings
5. Basic Interview Questions
6. Beginner DSA Problems

"""

# Question 1: Second Largest Element


arr = [7, 3, 9, 2, 8]
arr.sort()
print("Second Largest:", arr[-2])


# Question 2: Replace Alternate Elements

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
arr[::2] = [10,20,30,40,50,60]
print(arr)



# Question 3: Reverse Slicing


arr = [1,2,3,4,5]
print(arr[3:0:-1])



# Question 4: Function with List


def func(val, values):
    values[0] = 44

t = 3
v = [1,2,3]

func(t, v)
print(t, v[0])


# Question 5: Pop Last Element of Every Row
# ==========================================

matrix = [
    [1,2,3,4],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]
]

for row in matrix:
    print(row.pop())


# Question 6: List Aliasing

fruit_list1 = ['Apple','Berry','Cherry','Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"

total = 0

for lst in (fruit_list1, fruit_list2, fruit_list3):
    if lst[0] == "Guava":
        total += 1
    if lst[1] == "Kiwi":
        total += 20

print(total)


# ==========================================
# Question 7: Zip Function


for i, j in zip(range(1,6), range(5,0,-1)):
    if i == 3:
        continue
    print(i, j)

# Question 8: Tuple Length
# ==========================================

init_tuple = ()
print(len(init_tuple))

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print(init_tuple_a == init_tuple_b)


# ==========================================
# Question 9: Dictionary Practice


d = {(1,2):1, (2,3):2, (4,5):3}
print(d[(4,5)])

fruit = {}

def addone(item):
    if item in fruit:
        fruit[item] += 1
    else:
        fruit[item] = 1

addone("Apple")
addone("banana")
addone("apple")

print(len(fruit))
print(fruit)


# Question 10: Move Zeros

def move_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr

arr = [1,0,2,0,4,0,5]
print(move_zeros(arr))



# Question 11: Common Elements

A = [1,2,3]
B = [2,2,4]
C = [2,5,2]

for i in A:
    if i in B and i in C:
        print(i)


# Question 12: Maximum Consecutive Ones

nums = [1,1,0,1,1,1]

count = 0
maximum = 0

for i in nums:
    if i == 1:
        count += 1
        maximum = max(maximum, count)
    else:
        count = 0

print(maximum)


# Question 13: Palindrome

arr = [1,2,3,2,1]

if arr == arr[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Question 14: Reverse String

text = "Hello"

reverse = ""

for i in range(len(text)-1, -1, -1):
    reverse += text[i]

print(reverse)


# Question 15: Remove Duplicate Characters


text = "hello"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)
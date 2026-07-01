# var = [7, 3, 9, 2, 8]
# var.sort()
# print (var[-2])

# data = input()
# freq = {}
# for digit in data:

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# # print(a[::2])
# a[::2] = 10,20,30,40,50,60
# print(a)


# a = [1,2,3,4,5]
# print(a[3:0:-1])


# def func(val, values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t, v[0])


# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())


# # def f(i, val = []):
# #     val.append(i)
# #     print (val)
# # f(1)
# # f(2)
# f(3)



# arr = [1,2,3,4,5,6]
# for i in range(1, 6):
#     arr[i-1] = arr[i]
# for i in range(0, 6):
    #  print(arr[i], end = " ")

# List alising
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)     




# Question
# 1  5
# 2  4
# 4  2
# 5  1

# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i,j)


# init_tuple = ()
# print(init_tuple.__len__())



# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)


# l = [1,2,3]
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
# print(init_tuple)


# a = {(1,2):1, (2,3):2, (4,5):3}
# print(a[4,5])

# a = {'a':1, 'b':2, 'c':3}
# print(a['a','b'])




# fruit ={}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1   #{'Apple':1, 'Banana':1, 'apple':1 }

# addone('Apple')
# addone('banana')
# addone('apple')
# print(len(fruit))
# print(fruit)


# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1

# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)


# a={}
# a[1] = 1
# a['1']=2
# a[1.0]=4
# print(a)
# sum=0
# for k in a:
#     sum += a[k]
# print(sum)



# a = {}
# a[(1,2,4)] = 8
# a[(4,2,1)] = 10
# a[(1,2)] = 12
# sum = 0
# for k in a:
#     sum += a[k]
# print(sum)
# print(a)


# box = {}
# jars = {}
# crates = {}
# box['buscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))



# print(int(3.14))
# # print(int(10+5j))
# print(int(True))
# print(int(False))
# # print(int('10.2'))
# print(int('4'))
# # print(int("prashant"))
# print(float(3))
# print(float(3.14))
# print(float(True))
# print(float(False))
# print(float('3.14'))
# print(float('4'))
# # print(float('name'))
# print(float((50+2j)))



# def move_zeros(arr):
#     j = 0

#     # Move all non-zero elements to the front
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             j += 1

#     return arr

# arr = [1, 0, 2, 0, 4, 0, 5]
# print(move_zeros(arr))


# val = [0,1,0,3,12]
# for i in val:
#     if i == 0:
#         val.remove(i)
#         val.append(i)
# print(val)


# A = [1, 2, 3]
# B = [2, 2, 4]
# C = [2, 5, 2]
# for i in A:
#     if i in B and i in C:
#         print(i)


# Maximum consecutive Ones 
# nums = [1, 1, 0, 1, 1, 1]

# count = 0
# max_count = 0

# for i in nums:
#     if i == 1:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)


# # Palindrome Number
# A = [1,2,3,2,1]
# if A[:] == A[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 


# Reverse a string  
# str = "Hello"
# newname = ''
# for i in range(len(str),0,-1):
#     newname += str[i-1]
# print(newname)  


# Remove duplicates
str = "hello"
new_str = " " 
for i in str:
    if i not in new_str:
        new_str += i;
print(new_str)
#         new_str.append(i)
# print(new_str)
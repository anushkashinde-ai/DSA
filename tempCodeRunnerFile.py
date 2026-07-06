# import time
# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()



# import re
# count = 0
# pattern = re.compile('function')
# print(pattern)
# matcher = pattern.finditer("A function in python is defined by a def statement. The general synatx look like this: def function name ")
# print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...", i.end(),"...", i.group())
# print("Number of occurrences :",count)
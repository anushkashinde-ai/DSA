#positional arguement
# def msg(val1, val2):
#     print("Value 1 =",val1)
#     print("Value 2 =",val2)
# # calling function
# msg("admin", "help4code")

# keyword arguement
# def msg(val1, val2):
#     print("Value 1 =",val1)
#     print("Value 2 =",val2)
# # calling function
# msg(val1="admin", val2="help4code")

# default arhuement
# def city(cityName="Nashik"):
#     print("City name =", cityName)
# city("Mumbai")
# city("Delhi")
# city()


# Variable length arguement
# def cityName(*city):
#     print(city)
# cityName("Nagpur", "Nashik", "Pune", "Mumbai")
# def arithmatic(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div #return multiple value at the same time
# print(arithmatic(5,5))


# Nested loop
# for i in range(1,4):#row
#     for j in range(1,4):#col
#         print(i,end=" ")
#     print()

# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i,end=" ")
#     print()

# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(n+1-i,end=" ")
#     print()

# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     print(" * "*i)

# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, 1+i):
#         print(chr(64+i),end=" ")
#     print()



# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, 1+i):
#         print(i,end=" ")
#     print()



# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(" * ",end=" ")
#     print()




# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+j),end=" ")
#     print()




# import time
# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         time.sleep(2)
#         print(n+1-i,end=" ")
#     print()




# n = int(input("Enter value of n :"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(65+n-i),end=" ")
#     print()





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




# import re 
# count = 0
# matcher =  re.finditer("HI", "HIHIHIHI")
# print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...", i.end(),"...", i.group())
# print("Number of occurrences :",count)



# import re 
# obj = input("Enter any char :")
# objmatch=re.finditer(obj,"a7b @k9z")
# print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())




# import re 
# a = input("Enter string :")
# mtch = re.fullmatch(a, "pythonisvery")
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("there is no match")




# import re 
# a = input("Enter string :")
# mtch = re.search(a, "python is sss language")
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start()," ", mtch.end(), " ",mtch.group())
# else:
#     print("there is no match")



# import re
# mtch = re.findall('[^0-9a-zA-Z]', "abc3hdh5bhk7ZQ$&*")
# print(mtch)


# sub() function
# import re 
# obj = re.sub('[0-9]', 'X', '2345 ABCD Fabc deff')
# print(obj)


# subn() function
# import re
# obj = re.subn('[0-7]','@','abce36ebbs15')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replcement is=", obj[1])


# valid email or not
# import re
# s=input("Enter email id :")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@sitrc[.]org",s)
# if m != None:
#     print("valid email")
# else:
#     print("invalid email")


# import re
# s=input("Enter email id :")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m != None:
#     print("valid email")
# else:
#     print("invalid email")


# valid mob no
# import re
# mo = input("Enter mob no :")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj != None:
#     print("valid")
# else:
#     print("Invalid")



# import re
# a = input("Enter string to perform match opeartion")
# f = open("anushka.txt", 'r')
# c = f.read()
# mtch = re.search(a,c)
# print(mtch)
# if mtch != None:
#     print("match not found at beginning level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("No matching")



# RECURSION ==> When the main problem can be able to divide into similar sub problmes then use recursion
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)
# print(factorial(4))


# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng) -1]:
#         return False
#     return isPalindrome(strng[1:-1])
# print(isPalindrome("anushka"))



# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)
# print(power(2,2))


# def prodOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] *prodOfArray(arr[1:]) # 2,3
# print(prodOfArray([1,2,3,10]))


# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveRange(num -1)
# print(recursiveRange(6))



def fib(num):
    if (num < 2):
        return num
    return fib(num -1) + fib(num-2)
print(fib(4))
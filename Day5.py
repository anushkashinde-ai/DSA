# mydict = {
#     101: "Anushka",
#     102: "Riya",
#     103: "Shreya",
#     102: "Harsh",
#     104: "Piya",
#     101: "Ashish"
# }
# print(mydict)
# # print(type(mydict))
# # a = mydict[102]
# # print(a)

# # mydict[102] = "peter"
# # print(mydict)


# #  only print key x =0,1
# for i in mydict:
#     print(i)

# # only print values
# # for x in mydict.values():
# #     print(x)

# # for p,q in mydict.items():
# #     print(p,':',q)

# mydict["mob_no"] = 736735837
# print(mydict)



# mydict = {
#     101: "Anushka",
#     "profession": "developer",
#     "id": 1001
# }
# mydict.pop(101)
# print(mydict)


# mydict = {
#     "name": "Anushka",
#     "profession": "developer",
#     "id": 1001
# }
# newdict = mydict.copy()
# print(newdict)


# max value in dict
# dict = {
#     "A" :50,
#     "B" : 60,
#     "C" : 89,
#     "D" : 30
# }
# max_val = 1
# for i in dict.values():
#     if i > max_val:
#         max_val = i
# print(max_val)



# # Dict is empty
# d = {}
# if d:
#     print("Empty")
# else:
#     print("Not empty")


# Reverse a dict
# dict = {
#     "A" :50,
#     "B" : 60,
#     "C" : 89,
#     "D" : 30
# }
# rev ={}
# for key in dict:
#     rev[dict[key]] = key
# print(rev)


# Common key value pair in two dict
# d1 = {
#     "a":10,
#     "b":20,
#     "c":30
# }
# d2 = {
#     "a":10,
#     "b":25,
#     "c":30,
#     "d":40
# }
# common = {}
# for key in d1:
#     if key in d2 and d1[key] == d2[key]:
#         common[key] = d1[key]
# print(common)


# Linear search --> O(n)
# def linearSearch(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr=[1,2,3,4,5,6,7,8,9]
# target = 10
# result = linearSearch(arr,target) #calling function
# if result != -1:
#     print("Element found at index no =",result)
# else:
#     print("Element not found")


# Max and Min Elements:
# arr=[5,3,7,8,9]
# min = arr[0]
# max = arr[0]
# for i in range(1, len(arr)):
#     if(arr[i]) < min:
#         min = arr[i]

#     if(arr[i]) > max:
#         max = arr[i]

# print("Minimum :",min)
# print("Maximum :",max)


# Find majority element
arr = [2,2,1,2,3,2,2]
# for i in arr:
#     count = 0
#     for j in arr:
#         if i == j:
#             count += 1
        
#         if count > len(arr)/2:
#             print("Majority Element:",i)
#             break
#         else:
#             print("No majority")   


# File handeling ==>Whenever we want to use data for future purpose so we used file handeling concept 
# f = open("myfile.txt", "w")
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readable :",f.readable())
# print("writable :",f.writable())
# print("file closed :",f.closed)
# f.close()
# print("file closed :",f.closed)


# Performing write operation
# f = open("myfile.txt","a")
# f.write("\nPune is a smart city")
# f.write("\nNagpur is a smart city")
# f.write("\nBangalore is a smart city")
# f.write("\nNashik is a smart city")
# f.write("\nIndore is a smart city")
# f.close()
# print("file operation is done")


# inserting list
# f = open("newfile.txt","w")
# mylist = ["Anushka", " ", "Riya"," " ,"Shreya"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")


# reading data from a file
# f = open("myfile.txt","r")
# print(f.read())
# f.close()


# with open("myfile.txt", "w") as f:
#     f.write("amit\n")
#     f.write("prashant\n")
#     f.write("ashish\n")
#     print("file closed",f.closed)
# print("file closed:",f.closed)



# with open("myfile.txt", "r") as f:
#     content = f.read()
#     print(content)


# f1=open("img.png","rb") #read binary
# f2=open("Rossum.png","wb")
# data=f1.read()
# f2.write(data)


# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentID", "rollNo","name","mobNo"])

# studId = int(input("Enter student id :"))
# rollno = int(input("Enter student roll no :"))
# name = input("Enter student name :")
# mobno = int(input("Enter mob no :"))
# a.writerow([studId, rollno, name, mobno])
# print("student recoed has save")


# import csv
# f = open("student1.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["rollNo","name","mobNo","p1","p2","p3","total","percentage","email", "result"])

# rollno = int(input("Enter roll no :"))
# name = input("Enter name :")
# mobno = int(input("Enter mob no :"))
# p1 = int(input("Enter p1 marks :"))
# p2 = int(input("Enter p2 marks :"))
# p3 = int(input("Enter p3 marks :"))
# total = p1+p2+p3
# percentage = (total/3.0)
# email = input("enter email :")

# a.writerow([rollno,name,mobno,p1,p2,p3,total,percentage,email])
# print("Save")


# Queue
import sys
class Queue:
    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def enQueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue.pop(0))

    def frontPeek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue[0])

    def deleteQueue(self):
        self.myQueue = None

size = int(input("Enter the size of Queue :"))
queObj = Queue(size)
while True:
    print("1. enQueue")
    print("2. Display")
    print("3. deQueue")
    print("4. frontPeek")
    print("5. Delete Queue")
    print("6. Exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        value = int(input("Enter value to add in queue :"))
        queObj.enQueue(value)
    elif choice == 2:
        queObj.display()
    elif choice == 3:
        queObj.deQueue()
    elif choice == 4:
        queObj.frontPeek()
    elif choice == 5:
        queObj.deleteQueue()
    elif choice == 6:
        sys.exit()
    



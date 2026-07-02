# from abc import ABC, abstractmethod   #abstract base class
# class Help4code(ABC): #abstarct class
#     @abstractmethod
#     def training(self):  #abstract method
#         pass

#     @abstractmethod
#     def placement(self):
#         pass

# class Anushka(Help4code): #Single level inheritance
#         def training(self):  
#             print("C, C++, Java")

#         def placement(self):
#             print("Java Placement")

# class Ankush(Help4code): #Single level inheritance
#         def training(self):  
#             print("Python || Django")

#         def placement(self):
#             print("Python Placement")

# class Prashant(Help4code): #Single level inheritance
#         def training(self):  
#             print("machine learning")

#         def placement(self):
#             print("Data science Placement")

# obj1 = Anushka()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Prashant()
# obj3.training()
# obj3.placement()


# from abc import ABC, abstractmethod   #abstract base class
# class Irtc(ABC): #abstarct class
#     @abstractmethod
#     def bookTicket(self):  #abstract method
#         pass

# class Anushka(Irtc): #Single level inheritance
#         def bookTicket(self):  
#             print("Ticket Booked")

# class Ankush(Irtc): #Single level inheritance
#         def bookTicket(self):  
#             print("Ticket Booked")

# class makemyTrip(Irtc):
#      def bookTicket(self):
#         print("Welcome")
#         self.source = input("Enter source station : ")
#         self.destination = input("Enter destination name : ")
#         self.date = input("Enter date : ")
#         print(" ========================================== ")

# obj1 = Anushka()
# obj1.bookTicket()

# obj2 = makemyTrip()
# obj2.bookTicket()



# class Arithmetic:
#     def add(self, a):
#         print(a);
#     def add(self, a,b):
#         print(a + b)
#     def add(self, a, b, c):
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,10)


# class Arithmetic:
#     def __init__(self):
#         print("No arguement")
#     def __init__(self,a):
#         print("One arguement")
#     def __init__(self,a,b):
#         print("two arguement")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(2,2)


# class RBI:
#     def homeloan(self):
#         print("home loan 12%")

#     def carloan(self):
#         print("Interest 7%")

# class SBI(RBI): #Child class
#     def homeloan(self):
#         print("ROI 10.5%")
#         super().homeloan()

# sbiobj = SBI()
# sbiobj.homeloan()
# sbiobj.carloan()


#Constructor overriding
class father:
    def __init__(self):
        print("Father")

class child(father):
    def __init__(self):
        print("Child")
        super().__init__()

obj = child()
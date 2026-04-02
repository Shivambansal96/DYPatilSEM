# # # # # # # arr = [32, 5, 5, 231, 31, 33]

# # # # # # # for i in range(10):
# # # # # # #     print(arr[i])



# # # # # # try:
# # # # # #     a = int(input("Enter a number: "))
# # # # # #     for i in range(1, 11):
# # # # # #         print(f" Multiplication table of {a} is {a*i}")

# # # # # # except ValueError:
# # # # # #     # print(f"Error = {e}")
# # # # # #     print("Enter a valid Number.")
# # # # # #     # ValueError("Enter a valid Number.")

# # # # # # except KeyError:
# # # # # #     print("Enter a valid Key.")



# # # # # # name = "Shivam"
# # # # # # print(name[1:3])

# # # # # try:
# # # # #     a = int(input("Enter a number: "))
# # # # #     b = int(input("Enter another number: "))


# # # # #     res = a / b
# # # # #     print(f"Answer = {res}")

# # # # # except ZeroDivisionError:
# # # # #     raise Exception("Number cannot be divided by 0.")

# # # # # except ValueError:
# # # # #     raise ValueError("Enter a valid number.")

# # # # # except Exception as e:
# # # # #     print(f"Error = {e}")

# # # # # finally:
# # # # #     print("Apna kaam hogya")






# # # # # def addition(a= 1, b):
# # # # def addition(a, b, c, d, e=3):


# # # #     sum = a + b
# # # #     print(sum)

# # # # # addition(5, 10)
# # # # addition(6)





# # # # ##  ## # # # # OOPS Concept

# # # # myDict  = {
# # # #     'name' : "Shivam"
# # # # }


# # # # myDict['name'] # # Bracket Notation
# # # # myDict.name     # Dot Notation

# # # # class Student:
# # # #     name = "Shivam Bansal"

# # # #     def __init__(self, name="anonymous"):
# # # #         self.fullName = name

# # # #     # def __init__(self):
# # # #     #     pass

# # # # # s1 = Student() # an object is Constructed.
# # # # # # print(Student.name)
# # # # # # print(s1.name)
# # # # # # print("s1 = ", s1)


# # # # # s1 = Student("Sejal") # an object is Constructed.
# # # # # s2 = Student()

# # # # # print(s1.fullName)
# # # # # print(s2.fullName)

# # # # # print("-------------------")

# # # # # print("s1 = ", s1)
# # # # # print("s2 = ", s2)






# # # class Student:

# # #     # # # Default Constructor
# # #     # def __init__(self):
# # #     #     pass

# # #     # # Parameterized Constructor
# # #     # def __init__(self, name):
# # #     #     self.name = name


# # #     # Default Parameterized Constructor
# # #     def __init__(self, name="anonymous"):
# # #         self.name = name

# # # s1 = Student("Shivam")
# # # print(s1.name)

# # # s2 = Student()
# # # print(s2.name)

# # #     # # Non-Parameterized Constructor
# # #     # def __init__(self):
# # #     #     print("An object has been Created")


# # class Student:

# #     def __init__(self, name):
# #         self.name = name        

# #     def welcome(self):
# #         print("Welcome", self.name)

# # s1 = Student("Shivam")
# # s1.welcome()

# # s2 = Student("Tithee")
# # s2.welcome()

# # s3 = Student("Sejal")
# # s3.welcome()




# # class Student:

# #     def __init__(self, name, m1, m2, m3):
# #         self.name = name
# #         self.m1 = m1
# #         self.m2 = m2
# #         self.m3 = m3

# #     def get_avg(self):
# #         avg = (self.m1 + self.m2 + self.m3) / 3
# #         return avg

# #     def get_details(self):
# #         print(self.name, "Average Marks =" , self.get_avg())


# # s1 = Student("Shivam", 94, 96, 98)
# # s1.get_details()



# # # ## # # Practice Set 2 
# # class Student:

# #     clgName = "D Y Patil SEM"

# #     def __init__(self, name, marks):
# #         self.name = name
# #         self.marks = marks

# #     def display_Details(self):
# #         print(f"Name = {self.name}")
# #         print(f"Marks = {self.marks}")
# #         print(f"College_Name = {self.clgName}")
# #         # print(f"College Name = {Student.clgName}")

# #         print(f"PASSED = {self.is_pass()}")
# #         print()
# #         print("------------------------------------")
# #         print()


# #     # def is_pass(self):
# #     #     if self.marks >= 40:
# #     #         return True
# #     #     else:
# #     #         return False

# #     def is_pass(self):
# #         return self.marks >= 40
        
# # s1 = Student("Shivam", 90)
# # # del s1.name
# # # del s1
# # s1.display_Details()

# # s2 = Student("Mohini", 19)
# # s2.display_Details()


# # ## # # Static Methods

# # class Student:

# #     name = "Shivam"

# #     @staticmethod
# #     def __init__(self):
# #         print("Student Object Created.")

# # s1 = Student()



# class Employee:

#     def __init__(self, r, d, s):
#         self.r = r
#         self.d = d
#         self.s = s

#     def getDetails(self):
#         print(f"Role = {self.r}")
#         print(f"Dept = {self.d}")
#         print(f"Salary = {self.s}")

# e1 = Employee("Trainer", "IT", 100)
# e1.getDetails()

# class Engineer(Employee):

#     def __init__(self, name , age, r, d, s):
#         self.name = name
#         self.age = age
#         super().__init__(r, d, s)

#     def getDetails(self):
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         return super().getDetails()
    
# eng1 = Engineer("Winnie", 22, "Drama Karna", "Influencer", 9999)
# eng1.getDetails()


class Bank:

    def __init__(self, accNum, accPass):
        self.accNum = accNum
        self.__accPass = accPass

    def __getPassword(self):
        return self.__accPass
    
    def resetPassword(self):
        print("Old Password =", self.__getPassword())
        self.__accPass = "Jaa na change nahi karna"
        print("New Password =", self.__accPass)

b1 = Bank(143801000115559, "Shivam@321")
# print(f"Account Number = {b1.accNum}")
# print(f"Password = {b1.__accPass}")
# b1.__getPassword()

b1.resetPassword()


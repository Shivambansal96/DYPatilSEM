# # # # # # # # # age = 18


# # # # # # # # # if age >= 18:

# # # # # # # # #     if age >= 60:
# # # # # # # # #         print("Senior Citizen")
# # # # # # # # #     else:
# # # # # # # # #         print("Adult")

# # # # # # # # # else:
# # # # # # # # #     print("Minor")


# # # # # # # # userName = "Shivam@123"

# # # # # # # # print("@" not in userName)


# # # # # # # name = "Shivam"

# # # # # # # print(name[1:3])


# # # # # # list1 = [("Shivam", 99), ("Sejal", 100)]

# # # # # # print(list1[1][1])


# # # # # n = (5,)

# # # # # print(type(n))

# # # # a = "3"
# # # # b = "8"
# # # # c = a + b
# # # # print(c)

# # # # n = int(input("Enter a number: "))

# # # # for i in range(1, 6):
# # # #     if i == 3:
# # # #         continue

# # # #     print(i)


# # # # arr = [32, 65, 32, 13, 5, 7, 6, 33]

# # # # print(arr[0])
# # # # print(arr[1])
# # # # print(arr[2])
# # # # print(arr[3])
# # # # print(arr[4])
# # # # print(arr[5])
# # # # print(arr[6])
# # # # print(arr[7])

# # # # for i in range(10):
# # # #     print(i)
# # # #     print(arr[i])

# # # arr = [32, 65, 32, 13, 5, 7, 6, 33]

# # # for i in arr:
# # #     print(i)



# # i = 1

# # while i <= 10:
# #     i += 1
# #     print(i)

# #     i += 1



# name = "Hello " + "World"
# name = "Hello" + " World"
# name = "Hello" + " " + "World"

# print(name)





# def addition(a, b):
#     sum = a + b

#     return sum

# res = addition(5, 10)
# print(res)


def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact*= i

    return fact


# n = int(input())
n = 5
r = 3
# print(factorial())

num = factorial(n)
denom = factorial(n - r)

perm = num / denom

print(perm)

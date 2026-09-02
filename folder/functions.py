# def function():
#     print("Hello, from function")

# function()
# function()
# function()

# def function(fahreneit):
#     return (fahreneit - 32)* 5 / 9


# print(function(77))
# print(function(23))
# print(function(234))
# print(function(77))


# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", "Buddy", age = 5)


# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal="Dog")


# def myfuction(fruits):
#     for i in fruits:
#         print(i)

# my_fruits = ["apple", "Banana", "Kiwi"]

# print(myfuction(my_fruits))


# def countdown(n):
#     if n<0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(6)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# def myfunction(**args):
#     print("my name is ",  args)


# # myfunction("Dio", "dio", 12)


# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)

# my_function("Emil", "Tobias", "Linus")




def myfunction(greeting, *args):
    for i in args:
        print(greeting, i)

myfunction("Hello", "Dio", "DEko", "Asma")
# def kg_to_g(kg):
#     return(kg * 1000)

# print(kg_to_g(1))
# print(kg_to_g(30))


# def dio():
#     return "Hello Dio"

# d = dio();
# print(d)

# def ayaan():
#     return "Hello Ayaan"

# print(ayaan())



# def full_name(first_name):
#     return (first_name + " Mohamoud")

# print(full_name("Hawa"))

#parameter vs argumnets
# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("Emil") # "Emil" is an argument


# def fullnamw(fname, lname):
#   return (fname + lname)

# D = fullnamw("Abdikani", " Hassan")
# print(D)

# def mgc_dhmstrin(FirstName, LastName):
#    return (FirstName + LastName)

# print(mgc_dhmstrin("Abdikani", " Hassan"))



# def myFucntion(name = "friend"):
#    return ("Hello" + name)

# print(myFucntion())
# print(myFucntion("Dio"))


# def fullname(fname, lname=" Mohamoud"):
#     return (fname + lname)

# d = fullname("Abdikani")
# d1 = fullname("Abdikani", " Hassan")
# print(d)
# print(d1)

# def myFunction(country = "somalia"):
#    return ("i am from " + country)

# print(myFunction())
# print(myFunction("canada"))


# def myFunctions(name, animal):
#    print("i have a " + animal)
#    print("my " + animal + "'s name is " + name)

# #print(myFunctions("asad", "cat"))
# print(myFunctions(name="asad", animal="cat"))




def info(name, anima):
    print("i have " + anima)
    print("my cat's name is " + name)

d = info("Abdikani", "Cat")
print(d)
# def my_funstion(name):
#     for i in name:
#         print(i)
# names = ["Dio", "Deko"]
# my_funstion(names)




# # Create the fruits list
# fruits = ["apple", "Banana", "Cherry"]
# # Loop through fruits, break at "banana"

# for i in fruits:
#     if i == "Banana":
#         break
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i +=1


# i = 1
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i +=1



# names = ["Dio", "Deko", "NINA"]
# # x = names[2]
# # print(x)
# print(names[0])
# print(len(names))


# y = min(20,100,100)
# x = max(20,100,1000)
# print(y)
# print(x)
# numbers = [20,100,1000,20000]
# x = max(numbers)
# y = min(numbers)
# print(x)
# print(y)


# x,y,z = 2,3,4
# print(z)

# d,a,c=1,2,3
# print(c)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# x,y,z = 2,3,4
# print(z)




# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# x = 23

# def my_function():
#     return 2+x

# print(my_function())

# z = 2
# def my_function():
#     x = 23 #local variable
#     global y #global variable inside the function
#     y = 22
#     print(x)

# print(my_function(),  "loacl variable")
# print(y)
# print(y + z)



# x = 2
# y = 1.3
# z = 1j

# d = float(x)
# c = int(y)
# f = complex(x)


# print(d)
# print(c)
# print(f)

# print(type(d))
# print(type(c))
# print(type(f))




# a = """hbvsbvfhkvbhksfbkbsfbkvsfbksf
# vsfvsfkvbsfkbvskfbvs
# n sfkbvksf h"""
# print(a)


# a = "Abdikani, Hassan"#variable sometimes is like array
# print(a[7])





# a = "DIO "
# d = a.lower()
# print(d)
# x = d.upper()
# print(x)
# print(a.strip())#remove space/blank


# def my_function():
#     return 5 > 2
# if my_function():
#     print("yes")
# else:
#     print("nope")



# names = ["Deko", 'Dio', 'hawa']
# for i in names:
#     # if i == "Dio":
#     names.reverse()
#     print(i)

# list = ['apple', 'cherry', 'yaanyo', 'pasal']
# print(list[-4:1])


# def my_function():
#     names = ["Dio", "Hmdi", "Qanjo", "Deko"]
#     new_names = []

#     for i in names:
#         if i == "Qanjo":
#             continue    
#         new_names.append(i)
#         print(i.upper())

# my_function()

# for i in range(10):
#     print("DIO")
    
# print(list(range(10)))

# list [1,2,3,4]
# data_car = {
#     "name": "Dodge",
#     "brand": "Challenger",
#     "date": "2021"
# }

# print(data_car["brand"])
# print(len(data_car))
# print(type(data_car))
# print(type(list))


# info = dict(name = "dio", age = 23, )
# print(info)


#Python Iterators
# names = ("Dio", "Deko", "Asma")
# my_tier = iter(names)



#Create an Iterator
# class my_numbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x

# dio = my_numbers()
# my_iter = iter(dio)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))



# #Stope iteration
# class my_numbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <=20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration

# dio = my_numbers()
# my_iter = iter(dio)

# for i in my_iter:
#     print(i)


# from modules import info
# import datetime
# import modules

# dio = modules.mynumbers()
# my_iter = iter(dio)

# for i in my_iter:
#     print(i)

# x = datetime.datetime.now()
# print(x)


# x = modules.dio(5)
# print(x)


# x = dir(modules)
# print(x)

# x = modules.info["age"]
# print(x)

# print(info["name"])





# #MATH
# import math
# x = modules.pw(2,4)
# print(x)


# x = max(23,34,45)
# print(x)


# tupel = (23,34,556)
# print(max(tupel))

# y = abs(-233)
# print(y)

# tupel = abs(23,23,45,-234)
# print(tupel)


# x = math.sqrt(2)
# print(math.ceil(x))
# print(math.floor(x))




# try:
#     t = open("modules.py")
#     try:
#         t.write("" \
#         "def my_function():" \
#             "return 5+2")
#     except:
#         print("sonething went wrong when writing ")
# except:
#     print("sonething went wrong when opening the file")


# X = -1

# if X < 0:
#     raise Exception("sorry, no number below zer")


# x = input("enter number")

# if not type(x) is int:
#     raise Exception("Only integers are allowed")


# try:
#     f = open("DIO.TEXT")
#     try:
#         f.write("Magacaa")
#     except:
#         print("there is error writing in the file")
# except:
#     print("there is error opening file")
# finally:
#     f.close

# from .import DIO


# try:
#   f = open("DIO.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")



# t = 23
# r = 34
# x = f"the operation is  {t + (r * 3)}"
# print(x)


# x = 23

# t  = f"the price is {'expensive' if x > 20 else "cheap"}"
# print(t)



# x = "FRUITE"
# t = f"i hate {x.lower()}"
# print(t)


# n = "rting"
# for i in n:
#     print(i)
  
# n = "5"

# for i in n:
#     i+=1
#     for j in i:
#         j+=1
#         print(j)
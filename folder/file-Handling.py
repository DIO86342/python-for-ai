
# f = open(r"C:\Users\hp\Downloads\war.txt")
# print(f.read())


# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#     print(f.read())



# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#     print(f.readline())
#     print(f.readline())
#     f.close()


# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#     print(f.read(5))



# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#     for x in f:
#         print(x)


# f = open(r"C:\Users\hp\Downloads\war.txt", "b")
# print(f.read())


# "a" - Append - will append to the end of the file
# with open(r"C:\Users\hp\Downloads\war.txt", "a") as f:
#     f.write("Haka Walwalin")
    

# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#     print(f.read())




# "w" - Write - will overwrite any existing content
# with open(r"C:\Users\hp\Downloads\war.txt", "w") as f:
#         f.write("Woops! I have deleted the content!")

# with open(r"C:\Users\hp\Downloads\war.txt") as f:
#         print(f.read())


#Create a New File
#"x" - Create - will create a file, returns an error if the file exists
# f = open(r"C:\Users\hp\Downloads\war1.txt", "x")

#"a" - Append - will create a file if the specified file does not exists
# with open(r"C:\Users\hp\Downloads\war2.txt", "a") as f:
#     f.write("MA IMAQASHAA")

# with open(r"C:\Users\hp\Downloads\war1.txt") as f:
#     print(f.read())


#"w" - Write - will create a file if the specified file does not exists
# with open(r"C:\Users\hp\Downloads\war3.txt", "w") as f:
#     f.write("WA IKANAAA")

# with open(r"C:\Users\hp\Downloads\war3.txt") as f:
#     print(f.read())






#Delete a File
import os
# os.remove(r"C:\Users\hp\Downloads\war3.txt")


if os.path.exists(r"C:\Users\hp\Downloads\war2.txt"):
    os.remove(r"C:\Users\hp\Downloads\war2.txt")
else:
    print("file doesnot exist")





















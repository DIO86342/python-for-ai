import pandas as pd


# df = pd.read_excel("C:/Users/hp/Downloads/archive (8)/data.xlsx")
# #print(df)
# # print(df.to_string())
# pd.options.display.max_rows = 999
# print(df)

#print(df.head)
#print(df.describe())
# print(df.info)
#print(df.to_string())


# info= {
#     "name" : "Abdikani",
#     "Age" : 23,
#     "Batch" : "Cs"
# }



# info2 = {
#     "Names" : ["Abdikani", "Ahmed", "Ayaan"],
#     "Age" : [23, 20, 24]
# }
# #print(info)

# x = pd.DataFrame(info2)
# print(x)


# print(pd.__version__)

 

# array = [1,2,3,4,5]
# x = pd.Series(array)
# print(x)
# print(x[4])


# y = pd.Series(array, index=["A", "B", "C", "D", "E"])
# print(y)
# print(y["D"])




# names = {"NAME1" : "Ahmed",
#         "NAME2": "Ahmed",
#         "NAME3": "Ahmed",
#         "NAME3": "Ahmed"
# }

# x = pd.Series(names)
# print(x)


# track = {
#     "calories": [1200, 2000, 2140],
#     "protein" : [120, 180, 190]
# }


# x = pd.DataFrame(track, index=["Day1", "Day2", "Day3"])
# print(x)




# info = {
#     "Calories" : [1200, 2000, 3000],
#     "protein"  : ["Normal", "Good", "High"]
# }


# x = pd.DataFrame(info)
# # print(x)
# # print(x.loc["Day_1"])
# print(x.loc[[0,1,2]])
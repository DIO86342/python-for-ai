import pandas as pd


df = pd.read_excel("C:/Users/hp/Desktop/PythonProjects/python-for-ai/archive (8)/fitness_data_unformatted_issues.xlsx")


# print(df)
# print(df.head(10))
# print(df.tail())
# print(df.info())





#cleaning The Data.............


# x = df.dropna() #Remove emty cells, entire row
# print(x.to_string())

# df.fillna(130, inplace=True) #Another way of dealing with empty cells is to insert a new value instead.
# print(df.to_string())

# df.fillna({"Calories" : 130}, inplace=True)#Replace NULL values in the "Calories" columns with the number 130:
# df.fillna({"Pulse" : 100}, inplace=True)
# df.fillna({"Maxpulse" : 100}, inplace=True)
# print(df.to_string())




# print(df.to_string())
# x = df["Calories"].mean()#Calculate the MEAN, and replace any empty values with it:
# df.fillna({"Calories" : x}, inplace=True)
# y = df["Pulse"].mean()
# df.fillna({"Pulse":y}, inplace=True)
# print(df.to_string())



# x = df["Calories"].median()#Calculate the median, and replace any empty values with it:
# df.fillna({"Calories" : x}, inplace=True)
# y = df["Pulse"].median()
# df.fillna({"Pulse":y}, inplace=True)
# z = df["Maxpulse"].median()
# df.fillna({"Maxpulse": x}, inplace=True)
# print(df.to_string())



# df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
# print(df.to_string())



import matplotlib.pyplot as plt
x = df.dropna() #Remove emty cells, entire row

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
x.drop([22], inplace= True)
print(x.to_string())
x.plot()
plt.show()
# df.loc[7,"Duration"] = 50
# print(df.to_string())

# for i in df.index:
#     if df.loc[i,"Duration"] > 55:
#         df.loc[i, "Duration"] = 50
# print(df.to_string())
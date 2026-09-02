import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv")

new_path = path.dropna()
# print(new_path.head(20))

# x = new_path[['Age']]
# y = new_path['Salary']

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y,
#     test_size=0.2,
#     random_state=42
# )


# model = LinearRegression()

# model.fit(x_train, y_train)

# new_data = pd.DataFrame({'Age': [32,28,45]})

# prediction = model.predict(new_data)
# print(f"Model Predicted: {prediction}")
# print(f"Slope: {model.coef_[0]}")
# print(f"intercept:{model.intercept_}")
# # r2 = r2_score(y_test, prediction)
# # print(r2)








# #MULTIPLE LINEAR REGRESSION

# x = new_path[['Age', 'Years of Experience']]
# y = new_path['Salary']
# print(new_path.head())

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y,
#     test_size=0.2,
#     random_state=42
# )


# model = LinearRegression()
# model.fit(x_train, y_train)

# prediction = model.predict(x_test)

# r2 = r2_score(y_test, prediction)
# MAE = mean_absolute_error(y_test, prediction)

# print(f"MAE: {MAE}")
# print(f"R square :{r2}")


# # Tijaabinta xog cusub oo dhab ah (Banaanka ka weyn/kale)
# new_person = pd.DataFrame(
#     {
#         'Age': [32],
#         'Years of Experience': [5]
#     }
# )

# new_predict = model.predict(new_person)
# print(f"Model predicted: ${new_predict[0]:,.2f}")



# change_data = pd.get_dummies(
#     new_path,
#     columns=['Age', 'Years of Experience', 'Gender', 'Education Level', 'Job Title'],
#     drop_first=True,
#     dtype=int
# )
# # print(change_data.head())
# # print(change_data.columns())

# x = change_data.drop('Salary', axis=1)
# y = change_data['Salary']

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y,
#     test_size=0.2,
#     random_state=42
# )

# model = LinearRegression()
# model.fit(x_train, y_train)


# new_data = pd.DataFrame(
#     {
        
#     }
# )

# # prediction = model.predict(x_test)
# new_prdiction = model.predict(new_data)

# # r2 = r2_score(y_test, prediction)
# # MAE = mean_absolute_error(y_test, prediction)
# # print(f"R-Squared: {r2}")
# # print(f"Model predicted: {MAE}")






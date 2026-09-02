import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score


path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv")


new_path = path.dropna()



x = new_path[['Age']]
y = new_path['Salary']


#SPLIT THE DATA
x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
)


#CREATE THE MODEL
model = LinearRegression()

#TRAIN THE MODEL
model.fit(x_train, y_train)

#PREDICT UNSEEN DATA
prediction  = model.predict(x_test)

#EVALUATE THE DATA
# r2 = r2_score(y_test,prediction)

# print("R²:", r2)


# new_data = pd.DataFrame({
#     'Age': [20, 25, 30, 35, 40]
# })

# prediction = model.predict(new_data)

# print(prediction)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



path = pd.read_csv(r"C:\Users\hp\Downloads\Salary Data.csv")

new_path = path.dropna()

new_path['Age'] = new_path['Age'].astype(int)
new_path['Salary'] = new_path['Salary'].astype(int)

x = new_path[['Age']]
y = new_path['Salary']


# m, b, r, p, std_err = stats.linregress(x,y)

# def my_function(x):
#     return m*x+b
# model = list(map(my_function, x))

# plt.scatter(x,y)
# plt.plot(x,model)
# plt.show()

x_train,  x_test, y_train, y_test = train_test_split(
    x,y, 
    test_size=0.2,
    random_state=42
)


model = LinearRegression()
model.fit(x_train, y_train)


new_data = pd.DataFrame(
    {
        'Age' : [23,25]
    }
)

new_predicted  = model.predict(new_data)
# prediction = model.predict(x_test)

# r2 = r2_score(y_test, prediction)
# print(f"{r2*100:.2f}%")

print(new_predicted)





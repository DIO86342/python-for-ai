import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


path = pd.read_csv(r"C:\Users\hp\Downloads\archive (12)\Student_Performance.csv")


# print(path.head(10))


new_data = path.dropna()
new_data.drop_duplicates(inplace=True)
# print(new_data.duplicated().sum())
# print(new_data.isnull().sum())




x = new_data[['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']]
y = new_data['Performance Index']





x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)

r2 = r2_score(y_test, prediction)
MAE = mean_absolute_error(y_test, prediction)
MSA = mean_squared_error(y_test, prediction)
# print(f"R2:{r2*100:.2f}%")
# print(f"MAE: {MAE}")
# print(f"MSA: {MSA}")


print("Intercept:", model.intercept_)

for feature, coefficient in zip(x.columns, model.coef_):
    print(f"{feature}: {coefficient}")
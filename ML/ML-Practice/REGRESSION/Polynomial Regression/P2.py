import numpy as np
import pandas as pd

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


path = pd.read_csv(r"C:\Users\hp\Downloads\archive (12)\Student_Performance.csv")

new_data = path.dropna()
new_data = new_data.drop_duplicates()

x = new_data[
    [
        'Hours Studied',
        'Previous Scores',
        'Sleep Hours',
        'Sample Question Papers Practiced'
    ]
]

y = new_data['Performance Index']


# Split the original data
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# Create polynomial features
poly = PolynomialFeatures(degree=2)

x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)


# Train
model = LinearRegression()

model.fit(x_train_poly, y_train)


# Predict
prediction = model.predict(x_test_poly)


# Evaluate
r2 = r2_score(y_test, prediction)
MAE = mean_absolute_error(y_test, prediction)
MSE = mean_squared_error(y_test, prediction)

print(f"R2: {r2 * 100:.4f}%")
print(f"MAE: {MAE:.4f}")
print(f"MSE: {MSE:.4f}")
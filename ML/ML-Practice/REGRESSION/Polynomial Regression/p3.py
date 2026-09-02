import matplotlib.pyplot as plt
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


x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

poly = PolynomialFeatures(degree=1)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

model = LinearRegression()
model.fit(x_train_poly,y_train)

prediction = model.predict(x_test_poly)

r2 = r2_score(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)

print(f"R2: {r2*100:.2f}%")
print(f"{mae:.2f}")
print(f"{mse:.2f}")
# diff_err = prediction - y_test
# print(diff_err)


comparison = pd.DataFrame({
    'Actual' : y_test,
    'Predicted' : prediction
})

print(comparison.head(10))
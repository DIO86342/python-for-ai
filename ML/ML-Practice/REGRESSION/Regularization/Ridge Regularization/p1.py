import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
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

#POLYNOMIAL MODEL 
print("POLYNOMIAL MODEL")

poly_model = PolynomialFeatures(degree=1)
x_train_poly = poly_model.fit_transform(x_train)
x_test_poly = poly_model.transform(x_test)

model = LinearRegression()
model.fit(x_train_poly, y_train)

poly_predicator = model.predict(x_test_poly)

poly_R2 = r2_score(y_test,poly_predicator)
poly_MAE = mean_absolute_error(y_test, poly_predicator)
poly_MSE = mean_squared_error(y_test, poly_predicator)
print(f"{poly_R2*100:.2f}")
print(f"{poly_MAE}")
print(poly_MSE)
print(model.coef_)
print(model.intercept_)




#liner Regression
print("LINEAR MODEL")
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

linear_predicted = linear_model.predict(x_test)

linear_R2 = r2_score(y_test,linear_predicted)
linear_MAE = mean_absolute_error(y_test, linear_predicted)
linear_MSE = mean_squared_error(y_test, linear_predicted)
print(f"{linear_R2*100:.2f}")
print(f"{linear_MAE}")
print(linear_MSE)
print(linear_model.coef_)
print(linear_model.intercept_)




print("RIDGE MODEL")
#RIDGE REGRESSION
ridge_model = Ridge(alpha=1)
ridge_model.fit(x_train, y_train)


ridge_prediction = ridge_model.predict(x_test)


ridge_R2 = r2_score(y_test,ridge_prediction)
ridge_MAE = mean_absolute_error(y_test, ridge_prediction)
ridge_MSE = mean_squared_error(y_test, ridge_prediction)
print(f"{ridge_R2*100:.2f}")
print(f"{ridge_MAE}")
print(ridge_MSE)
print(ridge_model.coef_)
print(ridge_model.intercept_)
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso


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



lasso_model = Lasso(alpha=0.1)
lasso_model.fit(x_train, y_train)

prediction = lasso_model.predict(x_test)

R2 = r2_score(y_test, prediction)
MAE = mean_absolute_error(y_test, prediction)
MSE = mean_squared_error(y_test, prediction)

print(f"R2:{R2*100:.2F}%")
print(f"MAE: {MAE:.2F}")
print(f"MSE: {MSE:.2F}")


print(f"COEFF: {lasso_model.coef_}")
print(f"INTERCPT: {lasso_model.intercept_}")
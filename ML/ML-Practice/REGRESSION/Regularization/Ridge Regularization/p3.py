import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV

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



alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]


ridge_model = RidgeCV(
    alphas=alphas,
    cv=5
)
ridge_model.fit(x_train, y_train)

print("Best Alpha:" ,ridge_model.alpha_)

prediction = ridge_model.predict(x_test)



r2 = r2_score(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)


print("\nFINAL RIDGE MODEL")
print("-------------------------")

print("R²:", r2)
print("R²:", r2 * 100, "%")

print("MSE:", mse)

print("MAE:", mae)

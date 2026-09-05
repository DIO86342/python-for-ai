import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler


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


x_train, x_test, y_train, y_test =  train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)


scaler = StandardScaler()

x_train_scalar = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)


model = SVR(kernel="rbf")
model.fit(x_train_scalar, y_train)


prediction = model.predict(x_test_scaler)

r2 = r2_score(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)

print(f"R²: {r2:.4f}")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV
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
svr = SVR()

param_grid = {
    "kernel": ["rbf", "linear"],
    "C": [0.1, 1, 10, 100],
    "epsilon": [0.01, 0.1, 0.5, 1],
    "gamma": ["scale", "auto", 0.01, 0.1]
}


# param_grid = {
#     "kernel": ["rbf"],
#     "C": [1, 10, 100],
#     "epsilon": [0.1, 0.5],
#     "gamma": ["scale", 0.1]
# }

grid_search = GridSearchCV(
    estimator=svr,
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1
)

grid_search.fit(x_train_scalar, y_train)

print("Best Parameters:")
print(grid_search.best_params_)

print("Best CV R²:")
print(grid_search.best_score_)

best_svr = grid_search.best_estimator_

y_pred = best_svr.predict(x_test_scaler)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Test R²: {r2:.4f}")
print(f"Test MAE: {mae:.4f}")
print(f"Test MSE: {mse:.4f}")
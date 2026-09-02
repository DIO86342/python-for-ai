from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error




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


x_train, x_test, y_train, y_test  =train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)


lasso = Lasso()

param_grid = {
    "alpha": [0.001, 0.01, 0.1, 1, 10, 100]
}

grid_search = GridSearchCV(
    estimator=lasso,
    param_grid=param_grid,
    cv=5,
    scoring="r2"
)

grid_search.fit(x_train, y_train)

print("Best Alpha:", grid_search.best_params_)
print("Best CV R²:", grid_search.best_score_)

results = grid_search.cv_results_

print("\nAll Results:")
for alpha, score in zip(
    results["param_alpha"],
    results["mean_test_score"]
):
    print(f"Alpha: {alpha} → CV R²: {score:.4f}")

best_model = grid_search.best_estimator_

y_pred = best_model.predict(x_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\nFinal Test Performance:")
print(f"R²: {r2:.2%}")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split    
from sklearn.tree import DecisionTreeRegressor



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


for depth in [1, 2, 3, 4, 5, 6, 8, 10, None]:
    model = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    model.fit(x_train, y_train)

    train_prediction = model.predict(x_train)
    test_prediction = model.predict(x_test)

    train_r2 = r2_score(y_train, train_prediction)
    test_r2 = r2_score(y_test, test_prediction)


    print(
        f"Depth {depth} |" f"Train R2: {train_r2*100:.2f} |"  f"Test R2 {test_r2*100:.2f}"
    )
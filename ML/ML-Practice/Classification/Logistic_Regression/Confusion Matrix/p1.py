import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

data = pd.read_csv(r"C:\Users\hp\Downloads\archive (13)\Social_Network_Ads.csv")





df = data.dropna()

# print(df.to_string())





x = df[['Age', 'EstimatedSalary']]
y = df['Purchased']



x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
probabilties = model.predict_proba(x_test)

# print("Predcition")
# print(prediction)

# print("\nprobabilty")
# print(probabilty)


for row, probability, prediction in zip(
    x_test[['Age', 'EstimatedSalary']].itertuples(index=False),
    probabilties[:, 1],
    predictions
):
    print(
        f"Age: {row.Age}, "
        f"EstimatedSalary: {row.EstimatedSalary}, "
        f"Purchase Probability: {probability:.2%}, "
        f"Prediction: {prediction}"
    )



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix



data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Passed":       [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

x = df[["Hours_Studied"]]
y = df["Passed"]


x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)


predictions = model.predict(x_test)
probabilities = model.predict_proba(x_test)


# Threshold = 0.6,
# custom_prediction = (
#         probabilities[:,1] > Threshold,
# ).astype(int)


for threshold in [0.3, 0.5, 0.7, 0.9]:
    
    custom_predictions = (
        probabilities[:, 1] >= threshold
    ).astype(int)

    print(f"Threshold: {threshold}")
    print(f"Predictions: {custom_predictions}")
    print()

cm = confusion_matrix(y_test, predictions)

print(cm)
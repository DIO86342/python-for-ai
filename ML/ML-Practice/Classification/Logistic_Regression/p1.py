import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    'Hours' : [1,2,3,4,5,6,7,8,9],
    'Passed' : [0,0,0,0,0,1,1,1,1]
}


df = pd.DataFrame(data)


# print(df)

x = df[['Hours']] #contains the features.
y = df['Passed'] #contains the target/class.


model = LogisticRegression()
model.fit(x,y)

prediction = model.predict(x)

print(prediction)
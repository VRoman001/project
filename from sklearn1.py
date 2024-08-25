from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import confusion_matrix,accuracy_score
import numpy as np
import pandas as pd
np.random.seed(42)
count = 1000

age = np.random.uniform(1900,2024,count)
area = np.random.uniform(10,300,count)
rooms= np.random.randint(1,10,count)
distance = np.random.uniform(1,20,count)

price = (1000*area) + (rooms*4000) + ((2024-age)*500) - (distance * 2000)

date = pd.DataFrame({
    'age': age,
    'area': area,
    'rooms': rooms,
    'distance': distance,
    'price': price})
    
x = date.drop('price', axis=1)
y = date['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=42)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_train)

model = GradientBoostingRegressor(n_estimators=100,random_state=42)
model.fit(x_train, y_train)

prediction = model.predict(x_test)

new_date = pd.DataFrame({
    'age': [2022],
    'area': [100],
    'rooms': [4],
    'distance': [3]
})

final_date = sc.transform(new_date,)
prediction = model.predict(final_date)
print(prediction[0])

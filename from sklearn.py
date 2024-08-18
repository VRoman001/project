from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression
import numpy as np

np.random.seed(40)
count = 1000
rang = np.random.uniform(1,7,count)
kd_kill = np.random.uniform(0.1,2,count)
time = np.random.uniform(1,2000,count)
kd_win = np.random.randint(0.1,2,count)


high_risk = (rang < 3) | (kd_win < 0.5) | ((time < 200) & (kd_kill < 0.7))
higt_risk = high_risk.astype(int)

x = np.column_stack((rang,kd_win,time,kd_kill))
y = high_risk


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)

model = LogisticRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, prediction)

print(accuracy)

user1 = np.array([[4,0.9,330,0.9]])

prediction = model.predict(user1)
print('Тімейт поганий?:''ta' if prediction[0] else 'ni')

user2 = np.array([[5,0.5,120,0.4]])

prediction = model.predict(user2)
print('Тімейт поганий?:''ta' if prediction[0] else 'ni')
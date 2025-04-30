# 2025.04.30 파이썬
# bmi 예측 머신러닝에서 객체지향 실습
import numpy as np

np.random.seed(42)

height=np.random.normal(170,10,1000)
weight=np.random.normal(65,15,1000)
bmi=weight/(height/100)**2

X=np.vstack((height,weight)).T
Y=bmi

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

## 1. 함수를 이용한 머신러닝
'''
from p04bmifunctions import fit_decision_tree,predict_decision_tree

tree_model=fit_decision_tree(X_train,Y_train)
y_pred=predict_decision_tree(tree_model,X_test)
'''

## 2. 자체제작 클래스를 이용한 머신러닝

from p04bmiclass import MyDecisionTree
tree=MyDecisionTree(3)
tree.fit(X_train,Y_train)
y_pred=tree.predict(X_test)


## 3. 남이 만들어놓은 클래스 (DecisionTreeRegressor)를 이용한 머신러닝
'''
from sklearn.tree import DecisionTreeRegressor
tree=DecisionTreeRegressor()
tree.fit(X_train,Y_train)
y_pred=tree.predict(X_test)
'''

# 평가: 예측된 결과와, 정답 결과 비교
from sklearn.metrics import mean_squared_error

mse=mean_squared_error(y_pred,Y_test)
print(f"평균제곱오차(MSE) : {mse:.3f}")

for i in range(5):
    print(f"실제 BMI : {Y_test[i]:.2f} | 예측 BMI : {y_pred[i]:.2f}")


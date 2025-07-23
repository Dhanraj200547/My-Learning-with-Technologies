from sklearn import linear_model
import matplotlib.pyplot as plt
reg = linear_model.Ridge(alpha=.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
reg.coef_
reg.intercept_

plt.plot([0, 1], [reg.intercept_, reg.coef_[0] + reg.intercept_], color='red')
plt.scatter([0, 1], [0, 1], color='blue')
plt.scatter([0, 0, 1], [0, .1, 1], color='green')
plt.xlabel('x1')
plt.ylabel('y')
plt.title('Ridge Regression Example')
plt.show()
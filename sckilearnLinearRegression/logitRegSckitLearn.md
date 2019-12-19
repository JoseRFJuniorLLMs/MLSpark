>**Note:**
>This Readme has been automatically created by [zepppelin2md.py](https://github.com/bernhard-42/zeppelin2md).


# logitRegSckitLearn.json

---


_Input:_

```python
%pyspark
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
```


---


_Input:_

```python
%pyspark
reg = linear_model.LinearRegression()
```


---


_Input:_

```python
%pyspark
ar = np.array([[[1],[2],[3]], [[2],[4],[6]]])
```


---


_Input:_

```python
%pyspark
y = ar[1,:]
y
```


---


_Input:_

```python
%pyspark
x = ar[0,:]
x
```


---


_Input:_

```python
%pyspark
reg.fit(x,y)
```


---


_Input:_

```python
%pyspark
print('Coefficients: \n', reg.coef_)
```


---


_Input:_

```python
%pyspark
xTest = np.array([[4],[5],[6]])
xTest
```


---


_Input:_

```python
%pyspark
ytest =  np.array([[8],[10],[12]])

preds = reg.predict(xTest)
preds
```


---


_Input:_

```python
%pyspark
print('Coefficients: \n', reg.coef_)
```


---


_Input:_

```python
%pyspark
print("Mean squared error: %.2f" % mean_squared_error(ytest,preds))
```


---


_Input:_

```python
%pyspark
print("Variance score: %.2f" % r2_score(ytest,preds))
```


---


_Input:_

```python
%pyspark
plt.scatter(xTest,preds, color='black')
plt.plot(xTest,preds,color='blue', linewidth=3)


plt.show()
```


---


_Input:_

```python
%pyspark
print("Mean squared error: %.2f" % np.mean((regr.predict(test_data_X) - test_data_Y) ** 2))
```


import pandas as pd
import numpy as np


dir(np)

df = pd.Series(np.arange(1, 51,step=10))
print(df.axes)

np.arange(1, 52,10)


a = np.arange(0, 15).reshape(3,5)
a.axes

np.ones(3)
b= np.zeros((3,5))

b= np.ones((3,5))

a*b



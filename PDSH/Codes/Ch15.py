import pandas as pd
import numpy as np

rng = np.random.default_rng(seed=42)
ser = pd.Series(rng.integers(0, 10, size=4))
df = pd.DataFrame(rng.integers(0, 10, size=(3, 4)),
                  columns=['A', 'B', 'C', 'D'])
np.exp(ser)
np.sin(df * np.pi / 4)

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 39538223, 'Texas': 29145505,
                        'Florida': 21538187}, name='population')
population / area

area.index.union(population.index)


A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B
A.add(B, fill_value=0)


A = pd.DataFrame(rng.integers(0, 20, size=(2, 2)),
                 columns=['a', 'b'])
B = pd.DataFrame(rng.integers(0, 10, (3, 3)),
                 columns=['b', 'a', 'c'])
A + B


A.add(B, fill_value=A.values.mean())


A = rng.integers(10, size=(3, 4))
A - A[0]


df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]

df.subtract(df['R'], axis=0)


halfrow = df.iloc[0, ::2]  # return a series
df - halfrow

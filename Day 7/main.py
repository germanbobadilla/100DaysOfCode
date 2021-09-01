import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

plt.close("all")
ts = pd.Series(np.random.rand(1000),
               index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=["JavaScript", "Python", "Java", "Dart"])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')

plt.show()

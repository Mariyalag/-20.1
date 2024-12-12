import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

sns.set(style="whitegrid")
sns.scatterplot(data=data, x='x', y='y', color='green')
plt.title('Диаграмма точек')
plt.savefig('scatter_plot.png')
plt.show()


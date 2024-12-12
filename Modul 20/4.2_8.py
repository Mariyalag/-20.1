import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=1000)
sns.histplot(data, kde=True, color='purple')
plt.title('График распределения с KDE')
plt.savefig('distplot.png')
plt.show()
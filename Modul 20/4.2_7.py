import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("iris")
sns.pairplot(df, hue='species')
plt.title('Парный график для набора данных Iris')
plt.savefig('pairplot.png')
plt.show()
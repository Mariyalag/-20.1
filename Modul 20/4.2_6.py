import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("flights")
sns.regplot(x='passengers', y='year', data=df)
plt.title('График линейной регрессии')
plt.savefig('regplot.png')
plt.show()
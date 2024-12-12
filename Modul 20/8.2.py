
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
data = {
    'day': np.random.choice(days, size=200),
    'mandarin_consumption': np.random.poisson(lam=150, size=200)
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='mandarin_consumption', data=df, hue='day', palette='Oranges', dodge=True)
plt.title('Потребление мандаринов по дням недели перед Новым годом', fontsize=16)
plt.xlabel('День недели', fontsize=14)
plt.ylabel('Количество мандаринов', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

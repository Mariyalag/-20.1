import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y1 = np.random.randint(1, 10, size=10)
y2 = np.random.randint(1, 10, size=10)

plt.fill_between(x, y1, color="skyblue", alpha=0.4)
plt.fill_between(x, y2, color="orange", alpha=0.4)
plt.title('График с областями')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['Данные 1', 'Данные 2'])
plt.savefig('area_plot.png')
plt.show()

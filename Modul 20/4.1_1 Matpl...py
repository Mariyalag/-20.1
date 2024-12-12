import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')
plt.title('График синуса')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.legend()
plt.savefig('sin_plot.png')
plt.show()


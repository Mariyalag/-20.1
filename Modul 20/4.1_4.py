import matplotlib.pyplot as plt

labels = ['Сектор A', 'Сектор B', 'Сектор C', 'Сектор D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Круговая диаграмма распределения')
plt.savefig('pie_chart.png')
plt.show()

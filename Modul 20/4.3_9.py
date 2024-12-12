import plotly.express as px
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

fig = px.scatter(data, x='x', y='y', title='Интерактивная диаграмма точек', color_discrete_sequence=['blue'])
fig.write_html('interactive_scatter_plot.html')
fig.show()

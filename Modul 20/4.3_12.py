import plotly.express as px
import pandas as pd
import plotly.offline as pyo

df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 11, 12, 13],
    'text': ['A', 'B', 'C', 'D']
})

fig = px.scatter(df, x='x', y='y', text='text', title='График с подписями')
fig.update_traces(textposition='top center')
pyo.plot(fig, filename='scatter_plot.html', auto_open=True)
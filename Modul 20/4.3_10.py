import plotly.graph_objects as go
import numpy as np
import plotly.offline as pyo

x = np.linspace(0, 10, 100)
y = np.sin(x)
error = 0.1 + 0.1 * np.sqrt(x)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=y, mode='lines', name='sin(x)',
    line=dict(color='blue')))
fig.add_trace(go.Scatter(
    x=x, y=y + error, mode='lines', name='Upper Error',
    line=dict(color='red')))
fig.add_trace(go.Scatter(
    x=x, y=y - error, mode='lines', name='Lower Error',
    line=dict(color='red')))
fig.update_layout(title='График с ошибками', xaxis_title='X', yaxis_title='Y')
pyo.plot(fig, filename='3d_scatter_plot.html', auto_open=True)

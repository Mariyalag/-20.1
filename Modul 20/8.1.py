
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

pyo.init_notebook_mode()

dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='ME')
np.random.seed(42)
values = np.random.poisson(lam=200, size=len(dates))

data = pd.DataFrame({'Date': dates, 'Mandarin Consumption': values})

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data['Date'],
    y=data['Mandarin Consumption'],
    mode='lines+markers',
    name='Потребление мандаринов',
    line=dict(color='orange', width=4),
    marker=dict(size=8, symbol='star', color='yellow')
))

fig.update_layout(
    title='🎄 Потребление мандаринов на Новый год 🎉',
    xaxis_title='Дата',
    yaxis_title='Количество мандаринов',
    template='plotly_white',
    xaxis_rangeslider_visible=True,
    title_font=dict(size=24, color='green', family='Arial, sans-serif'),
    xaxis=dict(showgrid=True, gridcolor='lightgreen'),
    yaxis=dict(showgrid=True, gridcolor='lightgreen'),
)

fig.add_layout_image(
    dict(
        source="https://www.kindpng.com/picc/m/75-759828_christmas-tree-png-clipart-christmas-tree-illustration.png",
        xref="paper", yref="paper",
        x=0.5, y=0.5,
        sizex=0.5, sizey=0.5,
        xanchor="center", yanchor="middle",
        opacity=0.1,
        layer="below"
    )
)

pyo.plot(fig)

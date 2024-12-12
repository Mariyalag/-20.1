import plotly.express as px
import numpy as np
import pandas as pd
import plotly.offline as pyo

df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'z': np.random.rand(100)
})

fig = px.scatter_3d(df, x='x', y='y', z='z', title='3D график рассеяния')
pyo.plot(fig, filename='3d_scatter_plot.html', auto_open=True)
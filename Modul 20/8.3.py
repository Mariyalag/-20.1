
import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html

np.random.seed(42)
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

monthly_consumption = np.random.poisson(100, len(months))
monthly_data = pd.DataFrame({'Месяц': months, 'Потребление': monthly_consumption})

daily_consumption = np.random.poisson(20, len(days_of_week))
daily_data = pd.DataFrame({'День': days_of_week, 'Потребление': daily_consumption})

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Дашборд потребления мандаринов"),

    dcc.Graph(
        id='monthly-consumption',
        figure=px.bar(monthly_data, x='Месяц', y='Потребление', title='Потребление мандаринов по месяцам')
    ),

    dcc.Graph(
        id='daily-consumption',
        figure=px.box(daily_data, x='День', y='Потребление', title='Потребление мандаринов по дням недели')
    ),

    html.Div([
        html.H3("Дальнейшие шаги:"),
        html.Ul([
            html.Li(
                "Расширить функциональность приложения, добавив поддержку дополнительных форматов данных (например, CSV, Excel, базы данных)."),
            html.Li("Интегрировать приложение с веб-приложениями для более широкого доступа к данным."),
            html.Li(
                "Улучшить пользовательский интерфейс для повышения удобства использования и визуальной привлекательности."),
            html.Li(
                "Провести дополнительные тестирования и собрать обратную связь от пользователей для улучшения приложения.")
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)




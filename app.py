from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Hello World', style={'textAlign': 'center'})
])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
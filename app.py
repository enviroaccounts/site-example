from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go

app = Dash(__name__)

labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]


fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

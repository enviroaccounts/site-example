from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

app = Dash(__name__)

# Reading data
data_df = pd.read_csv("static/data/Pests.csv")

# Function to calculate the percentage
def calculate_percentage(val, total):
    percent = np.round((np.divide(val, total) * 100), 2)
    return percent

# Function to get pie chart data
def get_piechart_data():
    year_data = data_df.groupby('year')['count'].sum().reset_index()
    year_data['percent'] = calculate_percentage(year_data['count'], year_data['count'].sum())
    return year_data

# Function to get bar chart data for a specific year
def get_barchart_data(selected_year):
    year_data = data_df[data_df['year'] == int(selected_year)]
    year_grouped = year_data.groupby('Type', observed=False)['count'].sum().reset_index()
    year_grouped['percent'] = calculate_percentage(year_grouped['count'], year_grouped['count'].sum())
    return year_grouped

# Color palette for charts
colors = px.colors.qualitative.Plotly

# Initial figures
pie_chart_data = get_piechart_data()
fig_pie_chart = go.Figure(data=[go.Pie(labels=pie_chart_data['year'], values=pie_chart_data['percent'], hole=.3, name='Year', marker=dict(colors=colors))])

initial_barchart_data = get_barchart_data(pie_chart_data['year'].iloc[0])
fig_bar_chart = px.bar(initial_barchart_data, x='Type', y='percent', color_discrete_sequence=colors)

# Enable transitions
fig_bar_chart.update_layout(transition_duration=500)

# Layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(id='pie-chart', figure=fig_pie_chart),
    html.Div(children='Dash: A web application framework for your data.'),
    dcc.Graph(id='bar-chart', figure=fig_bar_chart)
])

# Callback for interactivity
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('pie-chart', 'clickData')]
)
def update_bar_chart(clickData):
    selected_year = clickData['points'][0]['label'] if clickData else pie_chart_data['year'].iloc[0]
    new_barchart_data = get_barchart_data(selected_year)
    return px.bar(new_barchart_data, x='Type', y='percent', color_discrete_sequence=colors).update_layout(transition_duration=500)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

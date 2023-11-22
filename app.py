from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

app = Dash(__name__)

# Reading data
data_df = pd.read_csv("static/data/Pests.csv")

# Function to calculate the percentage
def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""
    percent = np.round((np.divide(val, total) * 100), 2)
    return percent

# Function to create data for the pie chart
def data_creation(data, percent, class_labels, group=None):
    for index, item in enumerate(percent):
        data_instance = {}
        data_instance['category'] = class_labels[index]
        data_instance['value'] = item
        data_instance['group'] = group
        data.append(data_instance)

# Function to get pie chart data
def get_piechart_data():
    year_labels = ['2020', '2021', '2022']
    year_data = data_df.groupby('year')['count'].sum().values
    class_percent = calculate_percentage(year_data, np.sum(year_data))
    
    piechart_data = []
    data_creation(piechart_data, class_percent, year_labels)
    return piechart_data

# Extracting pie chart data
pie_chart_data = get_piechart_data()

# Assuming 'category' and 'value' are keys in the pie_chart_data
labels = [data['category'] for data in pie_chart_data]
values = [data['value'] for data in pie_chart_data]

# Create pie chart figure
fig_pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

# Bar chart
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig_bar_chart = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(id='pie-chart', figure=fig_pie_chart),
    html.Div(children='Dash: A web application framework for your data.'),
    dcc.Graph(id='bar-chart', figure=fig_bar_chart)
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

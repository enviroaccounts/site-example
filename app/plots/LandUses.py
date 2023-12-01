import dash
from dash import html, dcc

import pandas as pd
import plotly.graph_objects as go


def load_forest_land_use_data():
    """Loads forest land use change data."""
    return pd.read_csv("app/static/data/LandUseChange_Forest_1990_2016.csv")


def prepare_forest_land_use_chart_data(data_df):
    """Prepares data for the forest land use pie chart."""
    land_use_data = data_df.iloc[0,
                                 3:]  # land use columns start from the 4th column
    labels = land_use_data.index.tolist()
    values = land_use_data.values.tolist()
    return labels, values


def create_forest_land_use_pie_chart(labels, values):
    """Creates a pie chart for forest land use data."""
    return go.Figure(data=[go.Pie(labels=labels, values=values)])


def setup_dash_layout(app, fig_pie_chart):
    """Sets up the layout of the Dash app."""
    app.layout = html.Div(children=[
        html.Div([
            dcc.Graph(id='forest-land-use-pie-chart', figure=fig_pie_chart)
        ]),
        html.Div([
            html.H3(id='forest-land-use-pie-chart-description',
                    children='Land uses converted from forestland since 1990.')
        ])
    ], id='forest-land-use-pie-chart-layout')


def create_figure():
    # Load and prepare data
    data_df = load_forest_land_use_data()
    labels, values = prepare_forest_land_use_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_forest_land_use_pie_chart(labels, values)

    return fig_pie_chart


def create_app(app):
    """Creates and configures the Dash app."""

    fig_pie_chart = create_figure()

    # Setup layout
    setup_dash_layout(app, fig_pie_chart)

    return app


def init_dash(server):
    dash_app = create_app(
        dash.Dash(server=server, routes_pathname_prefix="/data/",))

    dash_app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>MGG My Custom footer</div>
    </body>
</html>
'''
    return dash_app

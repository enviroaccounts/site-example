from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go


def load_forest_land_use_data():
    """Loads forest land use change data."""
    return pd.read_csv("app/static/data/LandUseChange_Forest_1990_2016.csv")

def prepare_forest_land_use_chart_data(data_df):
    """Prepares data for the forest land use pie chart."""
    land_use_data = data_df.iloc[0, 3:]  # land use columns start from the 4th column
    labels = land_use_data.index.tolist()
    values = land_use_data.values.tolist()
    return labels, values

def create_forest_land_use_pie_chart(labels, values):
    """Creates a pie chart for forest land use data."""
    colors = {
        'Production grassland': '#1AA881',       #green
        'Built-up area': '#D186B0',              #pink
        'Wetland': '#1A80BA',                    # Dark blue
        'Cropland': '#F2E755',                   # Yellow
        'Grassland with woody biomass': '#DD7E33'  # Orange
    }

    # Map labels to colors
    pie_colors = [colors[label] for label in labels]

    pie_chart = go.Pie(
        domain={'x': [0, 1], 'y': [0, 1]}, #size of donut chart
        labels=labels, 
        values=values, 
        textinfo='percent',
        textposition='outside',
        insidetextorientation='auto',
        texttemplate='%{percent:.0%}',
        hoverinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>%{percent:.0%}<br>Total: %{value} ha<extra></extra>',
        hole=.65,
        marker=dict(colors=pie_colors),  # Apply custom colors
        showlegend=False,
        textfont=dict(size=30)  # Adjust text size inside pie chart
    )

    fig = go.Figure(data=[pie_chart])
    
    # Add scatter plot traces to mimic circular legend markers
    for label, color in zip(labels, pie_colors):
        fig.add_trace(go.Scatter(
            x=[None],  # No actual data points
            y=[None],
            mode='markers',
            marker=dict(color=color, size=20),
            name=label,
            textfont=dict(size=30) 
        ))

    # Update the layout to remove the background and add a light gray background
    fig.update_layout(
        width=500,  # Width of the canvas in pixels
       height=500,  # Height of the canvas in pixels
        legend=dict(
            orientation="h",
            x=0.15,
            y=-0.5,
            xanchor="left",
            yanchor="bottom",
            font=dict(size=30) 
        ),
        plot_bgcolor='rgba(0,0,0,0)',  # Making the plot background transparent
        paper_bgcolor='#F5F5F5',  # Light gray background for the entire graph
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),    
        hoverlabel=dict(
        font_size=25,          # Hover label font size 
        font_family="Inter"    # Change hover table font family 
    )
    )


    return fig

def create_figure():
    # Load and prepare data
    data_df = load_forest_land_use_data()
    labels, values = prepare_forest_land_use_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_forest_land_use_pie_chart(labels, values)


    return fig_pie_chart



def setup_dash_layout(app, fig_pie_chart):
    """Sets up the layout of the Dash app."""
    app.layout = html.Div(children=[
        html.Div([
            dcc.Graph(id='forest-land-use-pie-chart', figure=fig_pie_chart)
        ])
    ],id='forest-land-use-pie-chart-layout')

def create_app():
    """Creates and configures the Dash app."""
    app = Dash(__name__, suppress_callback_exceptions=True)
    fig_pie_chart = create_figure()
    setup_dash_layout(app, fig_pie_chart)
    return app

def init_dash(server):
    """Initializes a Dash app for a Flask server."""
    dash_app = create_app()
    dash_app.server = server
    dash_app.config.suppress_callback_exceptions = True
    dash_app.routes_pathname_prefix = "/data/"

    # Custom HTML layout
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
            <div>My Custom Header</div>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
            <div>My Custom Footer</div>
        </body>
    </html>
    '''
    return dash_app

# Example usage with a Flask server
if __name__ == '__main__':
    from flask import Flask
    server = Flask(__name__)
    app = init_dash(server)
    server.run(debug=True, host='0.0.0.0', port=8050)
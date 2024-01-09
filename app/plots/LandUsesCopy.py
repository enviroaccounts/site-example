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
        showlegend=True,
        textfont=dict(size=30)  # Adjust text size inside pie chart
    )

    fig = go.Figure(data=[pie_chart])
    
    # # Add scatter plot traces to mimic circular legend markers(Please dont remove this at the moment)
    # for label, color in zip(labels, pie_colors):
    #     fig.add_trace(go.Scatter(
    #         x=[None],  # No actual data points
    #         y=[None],
    #         mode='markers',
    #         marker=dict(color=color, size=10),
    #         name=label,
    #         textfont=dict(size=10) 
    #     ))

     # Update the layout to remove the background and add a light gray background
    fig.update_layout(
        autosize=True,  # Enable autosizing
        legend=dict(
            x=0.5,
            y=-0.1,
            xanchor="center",
            orientation="h",
            font=dict(size=10) 
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#F5F5F5',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),    
        hoverlabel=dict(
            font_size=25, 
            font_family="Inter"
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



from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_forest_land_use_data():
    """Loads forest land use change data."""
    return pd.read_csv("app/static/data/LandUseChange_ExoticForest_2008_2018.csv")

def prepare_forest_land_use_chart_data(data_df):
    """Prepares data for the forest land use pie chart."""
    # Extract data starting from the 'Producing Grassland' column
    land_use_data = data_df.iloc[0, 3:]
    labels = land_use_data.index.tolist()
    values = land_use_data.values.tolist()
    return labels, values

def create_forest_land_use_pie_chart(labels, values):
    """Creates a pie chart for forest land use data."""
    
    # Calculate percentages and create custom text labels
    total = sum(values)
    percents = [(v / total * 100) for v in values]
    custom_text = [f"<1%" if 0 < p < 1 else f"{p:.0f}%" for p in percents]
    
    colors = {
        'Production grassland': '#009E73',    
        'Fernland': '#FFB44F',             
        'Manuka and/or Kanuka': '#CC79A7',                    
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
        hovertemplate='<b>%{label}</b><br>%{percent:.0%}<br>Total: %{value}<extra></extra>',
        rotation=-30, 
        hole=.70,
        marker=dict(colors=pie_colors),  # Apply custom colors
        showlegend=False,
        textfont=dict(size=22,family="Overused Grotesk, sans-serif",color='#898989')  # Adjust text size inside pie chart
    )

    fig = go.Figure(data=[pie_chart])
    
    # Add scatter plot traces to mimic circular legend markers(Please dont remove this at the moment)
    for label, color in zip(labels, pie_colors):
        fig.add_trace(go.Scatter(
            x=[None],  # No actual data points
            y=[None],
            mode='markers',
            marker=dict(color=color, size=15),
            name=label,
            textfont=dict(size=15,family="Overused Grotesk, sans-serif",color='#898989') 
        ))


    fig.update_layout(
        autosize=True,  # Enable autosizing
        margin=dict(l=0, r=0, t=0, b=0),
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
            font_size=15, 
            font_family="Overused Grotesk, sans-serif"
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
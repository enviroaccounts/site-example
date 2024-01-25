from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_rainfall_data_1990_2005():
    """Loads rainfall data for 1990-2005."""
    return pd.read_csv("app/static/data/1990-2005_AverageRainfall_Makaroa.csv")

def load_rainfall_data_2022():
    """Loads rainfall data for 2022."""
    return pd.read_csv("app/static/data/MonthlyRainfall_Makaroa_2022.csv")

def prepare_rainfall_chart_data(data_df_1990_2005, data_df_2022):
    """Prepares data for the rainfall bar chart."""
    rainfall_data_1990_2005 = data_df_1990_2005.iloc[0, 3:]
    rainfall_data_2022 = data_df_2022.iloc[0, 2:]
    
    months = rainfall_data_1990_2005.index.tolist()
    values_1990_2005 = rainfall_data_1990_2005.values.tolist()
    values_2022 = rainfall_data_2022.values.tolist()

    return months, values_1990_2005, values_2022

def create_rainfall_bar_chart(months, values_1990_2005, values_2022):
    """Creates a bar chart for rainfall data with comparative years."""
    fig = go.Figure()
    
    # Adding 1990-2005 average data as blue bars
    fig.add_trace(go.Bar(
        x=months, 
        y=values_1990_2005, 
        name='1990-2005 average rainfall',
        marker_color='#009E73'  
    ))

    # Adding 2022 data as grey bars
    fig.add_trace(go.Bar(
        x=months, 
        y=values_2022, 
        name='Monthly rainfall',
        marker_color='#80CFB9'  
    ))

    # Updating the layout of the chart
    fig.update_layout(
        margin=dict(l=0, r=20, t=0, b=0),
        xaxis=dict(
            tickfont_size=14,
            showgrid=True, 
            gridcolor='#d4d4d4' 
        ),
        yaxis=dict(
            title='Rainfall (mm)',
            titlefont_size=16,
            tickfont_size=14,
            dtick=50,  # Displaying a tick every 50mm
            gridcolor='#d4d4d4'  # Showing horizontal grid lines in grey
        ),
        legend=dict(
            x=0.5,  # Centering the legend horizontally
            y=-0.15,
            xanchor='center',
            orientation='h',  # Setting legend orientation to horizontal
            font=dict(size=12),
        ),
        barmode='group',
        bargap=0.15,  # Space between bars of different groups
        bargroupgap=0,  # No space between bars of the same group
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        paper_bgcolor='#F5F5F5',
    )

    # Adjusting bar width
    fig.update_traces(width=0.4)  # bar width

    return fig

def create_figure():
    # Load data
    data_df_1990_2005 = load_rainfall_data_1990_2005()
    data_df_2022 = load_rainfall_data_2022()
    # Prepare data
    months, values_1990_2005, values_2022 = prepare_rainfall_chart_data(data_df_1990_2005, data_df_2022)

    # Create pie chart
    fig_bar_chart = create_rainfall_bar_chart(months, values_1990_2005, values_2022)


    return fig_bar_chart



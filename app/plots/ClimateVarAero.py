import pandas as pd
import plotly.graph_objects as go

def load_rainfall_data_2000_2013():
    """Loads rainfall data for 2000-2013."""
    return pd.read_csv("app/static/data/2000-2013_AverageRainfall_WanakaAero.csv")

def load_rainfall_data_2022():
    """Loads rainfall data for 2022."""
    return pd.read_csv("app/static/data/MonthlyRainfall_WanakaAero_2022.csv")

def load_temp_data_2000_2013():
    """Loads temperature data for 2000-2013."""
    return pd.read_csv("app/static/data/2000-2013_AverageTemp_WanakaAero.csv")

def load_temp_data_2022():
    """Loads temperature data for 2022."""
    return pd.read_csv("app/static/data/MonthlyTemp_WanakaAero_2022.csv")

def prepare_temp_chart_data(data_df_2000_2013, data_df_2022):
    """Prepares data for the temperature line chart."""
    temp_data_2000_2013 = data_df_2000_2013.iloc[0, 3:]
    temp_data_2022 = data_df_2022.iloc[0, 2:]
    
    values_temp_2000_2013 = temp_data_2000_2013.values.tolist()
    values_temp_2022 = temp_data_2022.values.tolist()

    return values_temp_2000_2013, values_temp_2022



def prepare_rainfall_chart_data(data_df_2000_2013, data_df_2022):
    """Prepares data for the rainfall bar chart."""
    rainfall_data_2000_2013 = data_df_2000_2013.iloc[0, 3:]
    rainfall_data_2022 = data_df_2022.iloc[0, 2:]
    
    months = rainfall_data_2000_2013.index.tolist()
    values_2000_2013 = rainfall_data_2000_2013.values.tolist()
    values_2022 = rainfall_data_2022.values.tolist()

    return months, values_2000_2013, values_2022

def create_rainfall_temp_chart(months, rainfall_2000_2013, rainfall_2022, temp_2000_2013, temp_2022):
    """Creates a combined bar and line chart for rainfall and temperature data."""
    fig = go.Figure()
    
    # Adding rainfall data as bars
    fig.add_trace(go.Bar(
        x=months, 
        y=rainfall_2000_2013, 
        name='2000-2013 average rainfall',
        marker_color='#009E73'  # Blue color
    ))
    fig.add_trace(go.Bar(
        x=months, 
        y=rainfall_2022, 
        name='2022 Monthly rainfall',
        marker_color='#80CFB9'  # Grey color
    ))
    
    # Assigning them to the secondary y-axis (yaxis='y2')
    # Adding Temperature Lines with markers
    fig.add_trace(go.Scatter(
        x=months, 
        y=temp_2000_2013, 
        name='2000-2013 avg temp',
        mode='lines+markers',  # Adding markers
        line=dict(color='#009E73'),
        yaxis='y2'
    ))
    fig.add_trace(go.Scatter(
        x=months, 
        y=temp_2022, 
        name='2022 monthly temp',
        mode='lines+markers',  # Adding markers
        line=dict(color='#80CFB9'),
        yaxis='y2'
    ))
    
    # Updating the layout of the chart
    fig.update_layout(
        xaxis=dict(
            tickfont_size=14,
            showgrid=True,# Displaying a tick every 20mm
            gridcolor='#dee2e6'
        ),
        yaxis=dict(
            title='Rainfall (mm)',
            titlefont_size=16,
            tickfont_size=14,
            dtick=20,  # Displaying a tick every 20mm
            gridcolor='#dee2e6'  # Showing horizontal grid lines in grey
        ),
        legend=dict(
            x=0.5,  # Centering the legend horizontally
            y=-0.1,
            xanchor='center',
            orientation='h',  # Setting legend orientation to horizontal
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
        ),
        barmode='group',
        bargap=0.15,  # Space between bars of different groups
        bargroupgap=0,  # No space between bars of the same group
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        paper_bgcolor='#F5F5F5',
    )
    
    # Adding secondary y-axis for Temperature
    fig.update_layout(
        yaxis2=dict(
            title='Temperature (℃)',
            titlefont_size=16,
            tickfont_size=14,
            dtick=5,
            overlaying='y',
            side='right',
        )
    )

    # Adjusting bar width separately
    for trace in fig.data:
        if isinstance(trace, go.Bar):
            trace.width = 0.4  # Adjust bar width

    return fig


def create_figure():
    # Load and prepare data
    data_df_rain_2000_2013 = load_rainfall_data_2000_2013()
    data_df_rain_2022 = load_rainfall_data_2022()
    data_df_temp_2000_2013 = load_temp_data_2000_2013()
    data_df_temp_2022 = load_temp_data_2022()

    months, rain_2000_2013, rain_2022 = prepare_rainfall_chart_data(data_df_rain_2000_2013, data_df_rain_2022)
    temp_2000_2013, temp_2022 = prepare_temp_chart_data(data_df_temp_2000_2013, data_df_temp_2022)

    combined_bar_and_line_chart = create_rainfall_temp_chart(months, rain_2000_2013, rain_2022, temp_2000_2013, temp_2022)



    return combined_bar_and_line_chart
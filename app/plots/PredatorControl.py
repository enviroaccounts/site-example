import pandas as pd
import plotly.graph_objects as go

def load_predator_data():
    """Loads predator control data."""
    return pd.read_csv("app/static/data/Predator_control.csv")

def prepare_predator_chart_data(data_df):
    """Prepares data for the predator control chart."""
    years = data_df['Year']
    traps_caught = data_df['Number of Active Traps']
    pests_caught = data_df['Pests Caught']
    catch_rate = data_df['Catch Rate']

    return years, traps_caught, pests_caught, catch_rate

def create_predator_control_chart(years, traps_caught, pests_caught, catch_rate):
    """Creates a combined bar and line chart for predator control data."""
    fig = go.Figure()

    # Adding Number of Active Traps and Pests Caught as bars on the primary y-axis
    fig.add_trace(go.Bar(
        x=years,
        y=traps_caught,
        name='Number of Active Traps',
        marker_color='#009E73' 
    ))
    fig.add_trace(go.Bar(
        x=years,
        y=pests_caught,
        name='Pests Caught',
        marker_color='#80CFB9'  
    ))

    # Adding Catch Rate as a line on the secondary y-axis
    fig.add_trace(go.Scatter(
        x=years,
        y=catch_rate,
        name='Catch Rate',
        mode='lines+markers',
        line=dict(color='#FFB44F'), 
        yaxis='y2'
    ))

    # Updating the layout of the chart
    fig.update_layout(
        margin=dict(l=80, r=80, t=0, b=0),
        xaxis=dict(
            title='Year',
            tickfont_size=14,
            showgrid=True,
            gridcolor='#dee2e6',
            dtick=1
        ),
    yaxis=dict(
        title='Number of traps or pests caught (#)',
        titlefont_size=16,
        tickfont_size=14,
        range=[0, 8000], 
        dtick=1000,  
        gridcolor='#dee2e6'
    ),
    yaxis2=dict(
        title='Average catch rate (catches/trap/year)',
        titlefont_size=16,
        tickfont_size=14,
        range=[0, 1.8],  
        tickmode='linear', 
        tick0=0,  
        dtick=0.2,  
        overlaying='y',
        side='right'
    ),
        legend=dict(
            x=0.5,
            y=-0.3,
            xanchor='center',
            orientation='h',
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            font=dict(size=12),
            itemclick=False,  
            itemdoubleclick=False 
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#F5F5F5',
    )

    # Adjusting bar width separately
    for trace in fig.data:
        if isinstance(trace, go.Bar):
            trace.width = 0.4

    return fig

def create_figure():
    # Load and prepare data
    data_df_predator = load_predator_data()
    years, traps, pests, catch_rate = prepare_predator_chart_data(data_df_predator)

    combined_bar_and_line_chart = create_predator_control_chart(years, traps, pests, catch_rate)

    return combined_bar_and_line_chart

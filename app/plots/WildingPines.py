from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_wildingpines_data():
    """Loads Wilding Pines control work data."""
    data = pd.read_csv("app/static/data/WildingPines.csv")
    return data

def prepare_wildingpines_chart_data(data_df):
    """Prepares chart data for Wilding Pines control work."""
    # Dropping rows with NaN values
    data_df = data_df.dropna()

    years = data_df['Year'].tolist()
    days_operating = data_df['No. of days operating'].astype(int).tolist()
    area_covered = data_df['Total area covered (ha)'].str.replace(',', '').astype(float).tolist()
    return years, days_operating, area_covered

def create_wildingpines_bar_chart(years, days_operating, area_covered):
    """Creates a grouped bar chart for Wilding Pines data."""
    fig = go.Figure(
        data=[
            go.Bar(name='Number of days control work was carried out', x=years, y=days_operating, yaxis='y', offsetgroup=1, marker_color='#f59f00'),
            go.Bar(name='Area covered by WCIS control work', x=years, y=area_covered, yaxis='y2', offsetgroup=2, marker_color='#339af0')
        ],
        layout={
            'yaxis': {
                'title': 'Days Operating',
                'range': [0, 250],
                'dtick': 50,
                'showgrid': True,  
                'gridcolor': 'white'  
            },
            'yaxis2': {
                'title': 'Area Covered (ha)',
                'overlaying': 'y',
                'side': 'right',
                'range': [0, 16000],
                'dtick': 2000,
                'showgrid': True,  
                'gridcolor': '#e5e5e5' 
            },
            'legend': {
                'x': 0.5,
                'y': -0.1,
                'xanchor': 'center',
                'yanchor': 'top',
                'orientation': 'v'
            },
            'plot_bgcolor': 'rgba(0,0,0,0)',  # Transparent plot background
            'paper_bgcolor': '#F5F5F5' 
        }
    )

    fig.update_layout(barmode='group',
        xaxis=dict(
            dtick=1
        ),
        autosize=True, 
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            font=dict(size=11),
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#F5F5F5', 
        hoverlabel=dict(
            font_size=15, 
            font_family="Overused Grotesk, sans-serif",
        ))

    return fig

def create_figure():
    # Load and prepare data
    data_df = load_wildingpines_data()
    years, days_operating, area_covered = prepare_wildingpines_chart_data(data_df)

    # Create bar chart
    fig_bar_chart = create_wildingpines_bar_chart(years, days_operating, area_covered)


    return fig_bar_chart



from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go


def load_predator_data():
    """Loads data about predator types."""
    data = pd.read_csv("app/static/data/Predator_type.csv")
    return data

def prepare_predator_chart_data(data_df):
    """Prepares data for the predator pie chart."""
    labels = data_df.iloc[:, 0].tolist()
    values = [float(str(value).strip()) for value in data_df.iloc[:, 1].tolist()]
    return labels, values

def create_predator_pie_chart(labels, values):
    """Creates a pie chart for predator data."""
    colors = {           #pink
        'Hedgehog': '#009E73',                   # Yellow
        'Mouse': '#D55E00',  # Orange
        'Possum': '#56B4E9',       #green
        'Ferret': '#CC79A7',                    # Dark blue
        'Other': '#F0E442',  # Orange
        'Rabbit': '#0072B2',              #pink
        'Rat': '#B3E2D5',                    # Dark blue
        'Stoat': '#FFB44F',                   # Yellow
    }
    
    # Map labels to colors
    pie_colors = [colors[label] for label in labels]

    pie_chart = go.Pie(
        domain={'x': [0, 1], 'y': [0, 1]},
        labels=labels,
        values=values,
        textinfo='percent',
        textposition='outside',
        insidetextorientation='auto',
        hoverinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>%{percent:.0%}<br>Total: %{value}<extra></extra>',
        hole=.70,
        rotation=-50, 
        marker=dict(colors=pie_colors),  # Apply custom colors
        showlegend=True,
        textfont=dict(size=18,family="Overused Grotesk, sans-serif",color='#898989')
    )
    

    fig = go.Figure(data=[pie_chart])
    
    
        
    # # Add scatter plot traces to mimic circular legend markers(Please dont remove this at the moment)
    # for label, color in zip(labels, pie_colors):
    #     fig.add_trace(go.Scatter(
    #         x=[None],  # No actual data points
    #         y=[None],
    #         mode='markers',
    #         marker=dict(color=color, size=15),
    #         name=label,
    #         textfont=dict(size=18,family="Overused Grotesk, sans-serif",color='#898989') 
    #     ))
    fig.update_layout(
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            x=0.5,  # Center the legend
            y=-0.15,  # Position the legend below the chart
            xanchor='center',
            yanchor='top',
            orientation='h',  # Keep the legend horizontal
            font=dict(size=12),
            itemclick=False,  
            itemdoubleclick=False 
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
    data_df = load_predator_data()
    labels, values = prepare_predator_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_predator_pie_chart(labels, values)


    return fig_pie_chart



from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_energy_consumption_data():
    """Loads energy consumption data by location."""
    data = pd.read_csv("app/static/data/GHG_emissions_energy_by_location.csv")
    return data

def prepare_energy_consumption_chart_data(data_df):
    """Prepares data for the energy consumption pie chart."""
    # Skipping the 'Total' row and unnecessary columns
    energy_data = data_df[:-1][['Substation', 'kWh']]
    labels = energy_data['Substation'].tolist()
    values = [float(value.replace(',', '').strip()) for value in energy_data['kWh']]
    return labels, values

def create_energy_consumption_pie_chart(labels, values):
    """Creates a pie chart for energy consumption data."""
    colors = {
        'Cardrona': '#F0E442',      
        'Camp Hill': '#009E73',           
        'Queensberry': '#FFB44F',               
        'Wānaka': '#56B4E9',             
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
        hole=.70,
        marker=dict(colors=pie_colors),  # Apply custom colors
        showlegend=True,
        textfont=dict(size=15,family="Overused Grotesk, sans-serif",color='#898989')  # Adjust text size inside pie chart
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

     # Update the layout to remove the background and add a light gray background
    fig.update_layout(
        autosize=True,  # Enable autosizing
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            x=0.5,
            y=-0.1,
            xanchor="center",
            orientation="h",
            font=dict(size=11),
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
        ),
    )

    return fig

def create_figure():
    # Load and prepare data
    data_df = load_energy_consumption_data()
    labels, values = prepare_energy_consumption_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_energy_consumption_pie_chart(labels, values)


    return fig_pie_chart



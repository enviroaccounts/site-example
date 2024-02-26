from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_builtup_area_data():
    """Loads land use change data for built-up areas."""
    return pd.read_csv("app/static/data/LandUseChange_BuildUp_1990_2016.csv")

def prepare_builtup_area_chart_data(data_df):
    """Prepares data for the built-up area land use pie chart."""
    # Extracting data from 'Forest' column onwards
    builtup_area_data = data_df.iloc[0, 3:]
    labels = builtup_area_data.index.tolist()
    values = builtup_area_data.values.tolist()
    return labels, values

def create_builtup_area_pie_chart(labels, values):
    """Creates a pie chart for built-up area land use data."""
    # Calculate percentages and create custom text labels
    total = sum(values)
    percents = [(v / total * 100) for v in values]
    custom_text = [f"<1%" if 0 < p < 1 else f"{p:.0f}%" for p in percents]
    
    colors = {       
        'Forest': '#FFB44F',                
        'Grassland with woody biomass': '#F0E442',  
        'Production grassland': '#009E73',     
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
        # texttemplate=custom_text  # Use custom text labels
        hole=.70,
        rotation=-30, 
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
            x=0.5,
            y=-0.1,
            xanchor="center",
            orientation="h",
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
    data_df = load_builtup_area_data()
    labels, values = prepare_builtup_area_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_builtup_area_pie_chart(labels, values)


    return fig_pie_chart

from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

def load_ghg_forestry_data():
    """Loads GHG forestry data."""
    data_df = pd.read_csv("app/static/data/GHG_emissions_and_removals_forestry.csv")
    return data_df

def prepare_ghg_forestry_bar_chart_data(data_df):
    """Prepares data for the GHG forestry vertical bar chart."""
    # Reshape the DataFrame for Plotly Express
    df_melted = data_df.melt(id_vars='Type', var_name='Year', value_name='Amount')
    df_melted['Amount'] = pd.to_numeric(df_melted['Amount'].str.replace(',', ''), errors='coerce')
    return df_melted

def create_ghg_forestry_bar_chart(data_df):
    """Creates a vertical bar chart for GHG forestry data."""
    # Custom color mapping
    custom_colors = {
        'Total sequestration (removal (tCO2e/yr))': '#1AA881',
        'Total emissions (from harvest (tCO2e/yr))': '#FFB44F'
    }

    fig = px.bar(data_df, x="Year", y="Amount", color='Type', barmode='relative',
                 hover_data={"Year": True, "Amount": ':.2f', "Type": True},
                 height=400,
                 color_discrete_map=custom_colors)

    # Customizing the layout
    fig.update_layout(
        margin=dict(l=80,r=40, t=20, b=0),
        legend=dict(
            x=1,
            y=-0.4,
            xanchor='right',
            yanchor='bottom',
            orientation='h',
            font=dict(size=12, family="Overused Grotesk, sans-serif", color='#898989')
        ),
        plot_bgcolor='#F5F5F5',
        paper_bgcolor='#F5F5F5',
        font=dict(size=18, family="Overused Grotesk, sans-serif", color='#898989')
    )

    # Customizing axes and grid
    fig.update_xaxes(
        gridcolor='#898989',
        showgrid=True,
        showline=True,
        linewidth=1,
        linecolor='#898989'
    )

    fig.update_yaxes(
        gridcolor='#898989',
        showgrid=True,
        showline=True,
        linewidth=1,
        linecolor='#898989'
    )
    
    fig.add_shape(
        # Line Top
        type="line", xref="paper", yref="paper",
        x0=0, y0=1, x1=1, y1=1,
        line=dict(color="#b6b6b6", width=1),
    )
    fig.add_shape(
        # Line Right
        type="line", xref="paper", yref="paper",
        x0=1, y0=0, x1=1, y1=1,
        line=dict(color="#b6b6b6", width=1),
    )

    return fig

def create_figure():
    # Load and prepare data
    data_df = load_ghg_forestry_data()
    df_melted = prepare_ghg_forestry_bar_chart_data(data_df)

    # Create bar chart
    fig_bar_chart = create_ghg_forestry_bar_chart(df_melted)

    return fig_bar_chart

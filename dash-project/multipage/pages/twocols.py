import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# Register page
dash.register_page(__name__)


# Load data
emissions_df = pd.read_csv("emissions.csv")
emissions_df = emissions_df.query("year >= 1950")

country_df = emissions_df.query("country == 'France'")


# Create components
header = html.H1("Page with two columns", style={"textAlign": "center"})

country_co2 = px.line(country_df, x="year", y="co2", title="CO2 emissions in France")

country_co2_split = px.line(
    country_df,
    x="year",
    y=["oil_co2", "gas_co2", "coal_co2"],
    title="CO2 emissions in France split",
)


# Define layout
layout = [
        header,
        dbc.Row(
            children=[
                dbc.Col(dcc.Graph(id="country_co2", figure=country_co2), width=8),
                dbc.Col(
                    dcc.Graph(id="country_co2_split", figure=country_co2_split), width=4
                ),
            ]
        ),
    ]

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


# Define layout
layout = [
        html.H1("A very minimal page", style={"textAlign": "center"}),
        dcc.Graph(
            id="country-co2",
            figure=px.line(
                country_df, x="year", y="co2", title="CO2 emissions in France"
            ),
        ),
    ]

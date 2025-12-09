import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# Register page
dash.register_page(__name__, path='/')

# Create components
header = html.H1("Welcome to our CO2 emissions Dashboard", style={"textAlign": "center"})

layout =dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                [header]
            )
        ],
        align="center",
        style={"height": "100vh"}
    )
])

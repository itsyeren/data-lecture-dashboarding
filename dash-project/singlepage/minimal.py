import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Create app
app = Dash()


# Load data
emissions_df = pd.read_csv("emissions.csv")
emissions_df = emissions_df.query("year >= 1950")

country_df = emissions_df.query("country == 'France'")


# Define layout
app.layout = [
    html.H1("CO2 emissions Dashboard", style={"textAlign": "center"}),
    dcc.Graph(
        id="country-co2",
        figure=px.line(
            country_df,
            x="year",
            y="co2",
            title="CO2 emissions in France"
        )
    )
]


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

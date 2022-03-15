import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

#####################################
#           IMPORT DATA             #
#####################################


#####################################
#           APP LAYOUT              #
#####################################
app.layout = html.Div([

    html.H1("Aplikacja webowo-dashowa Lukasza", style={'text-align': 'center'}),
    # break line
    html.Br()


])

import dash
import dash_bootstrap_components as dbc


app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions =True)

app.title = "Covid-19 prediction map"
server = app.server
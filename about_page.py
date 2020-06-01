import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app_components import header, footer

about_layout = html.Div([
    header,
    html.Div([],
             className="row")
    , footer
])

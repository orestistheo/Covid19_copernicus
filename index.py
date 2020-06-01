import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from map_page import map_layout
from about_page import about_layout
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        layout = map_layout
    elif pathname == '/about':
        layout = about_layout
    else:
        layout = '404'
    return layout


server = app.server


if __name__ == '__main__':
    app.config['suppress_callback_exceptions'] = True
    app.run_server(debug=True)


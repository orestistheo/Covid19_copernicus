import dash_bootstrap_components as dbc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

header = html.Div([
    # Header component
    # Navbar
    dbc.Nav(className="nav nav-pills", children=[
        ## home_page
        dbc.NavItem(html.Div([
            dbc.NavLink("HOME", href="/", id="about-popover", active=False),
            dbc.Popover(id="about", is_open=False, target="about-popover", children=[
                dbc.PopoverHeader("How it works")
            ])
        ])),
        ## about
        dbc.NavItem(html.Div([
            dbc.NavLink("ABOUT", href="/about", id="about-popover", active=False),
            dbc.Popover(id="about", is_open=False, target="about-popover", children=[
                dbc.PopoverHeader("How it works")
            ])
        ])),
    ], style={"backgroundColor": "#0060FF"})
]
)

footer = html.Div(
    id='footer-copyright',
    children=[
        html.Span(
            'Copyright © 2020 covid6gang',
            className='text-muted',
            style={'textAlign': 'center'}
        ),
        html.H5(""),
    ],
    className="row",
    style={
        'textAlign': 'center',
        'bottom': 0,
        'width': '100%',
        'padding': '10px 10px 0',
        # top right bottom left
        'margin': '20px  0px  10px  10px'
    }
)


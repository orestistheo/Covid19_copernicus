import dash_bootstrap_components as dbc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

header = html.Div([
    # Header component
    # Navbar
    dbc.Nav(className="nav nav-pills", children=[
        ## logo/home
        dbc.NavItem(html.Img(src=PLOTLY_LOGO, height="40px")),
        ## home_page
        dbc.NavItem(html.Div([
            dbc.NavLink("HOME", href="/covid_map", id="about-popover", active=False),
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
    ], style={"backgroundColor": "#00FFFF"})
]
)

footer = html.Div(
    id='footer-copyright',
    children=[
        html.Span(
            'Copyright © 2019 Jonathan Diamond',
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


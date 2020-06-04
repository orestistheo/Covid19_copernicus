import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app_components import header, footer

tab1_content = html.Div([
    html.Div([
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5("Charalampopoulou Dimitra"),
                            html.P(
                                "BA Business Administration & Information Systems"),
                            html.P(
                                "Role: Business planning & presentation",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5("Patsioura Vasiliki"),
                            html.P(
                                "Bsc in Chemistry"),
                            html.P(
                                "Role: Environmental analysis",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5("Stathaki-Amarantidou Ismini"),
                            html.P(
                                "MSc Pharmaceutical Analysis and Quality Control"),
                            html.P(
                                "Role: Study of viral behaviour and data gathering",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col()
    ],
        className="row"
        , style={'marginTop': '40px'}),
    html.Div([
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.A(html.H5("Christodoulakis Michalis"),
                                   href="http://linkedin.com/in/michalis-christodoulakis", className="card-title"),
                            html.P(
                                "Bsc Electrical and Computer Engineer"),
                            html.P(
                                "Role: Data gathering and model estimation",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.A(html.H5("Kolovos Spyros"), href="http://linkedin.com/in/spiros-kolovos", className="card-title"),
                            html.P(
                                "Bsc in Mechanical Engineering & Aeronautics"),
                            html.P(
                                "Role: Data gathering and model estimation",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col(),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.A(html.H5("Theodorakopoulos Orestis"),
                                   href="https://www.linkedin.com/in/orestis-theo/", className="card-title"),
                            html.P(
                                "Bsc Electrical and Computer Engineering"),
                            html.P("Role: Web app development and deployment",
                                   className="card-text",
                                   )
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )
        ),
        dbc.Col()
    ],
        className="row"
        , style={'marginTop': '40px'})
])

tab2_content = html.Div([
    dbc.Row([
        dbc.Col(html.Div(children=[
            html.Br(),
            html.H4("Overview"),
            html.Br(),
            html.Div("Recently published papers have suggested that, as happens with the diffusion of other viruses, air temperature"
                     " and humidity could alter the spread of COVID-19. Papers in discussion also suggest that air pollution, particularly"
                     " fine particulate matter, could be involved in the morbidity and mortality due to COVID-19 and might also play a"
                     " role in spreading the SARS-CoV-2 virus. This application, provided by the Copernicus Hackathon 2020 covid6gang team,"
                     " allows the user to explore some of these claims by plotting the average air temperature, UV radiation and humidity of "
                     "the most recent months, alongside climatological air pollution levels from the Copernicus Atmosphere Monitoring Service "
                     "and the mortality data obtained from Johns Hopkins University."),
            html.Br(), html.Br(),
            html.H4("Data source"),
            html.Div("Copernicus climate data store:"),
            html.A('https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset',
                   href='https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset', style={'color': '#0060FF', 'font-weight': 'bold'}),
            html.Br(), html.Br(),
            html.H4("Citations"),

            html.Br(),
            html.Span(
                "•	Qi, H.; Xiao, S.; Shi, R.; Ward, M. P.; Chen, Y.; Tu, W.; Su, Q.; Wang, W.; Wang, X.; Zhang, Z. COVID-19 Transmission in Mainland China Is Associated with Temperature and Humidity: A Time-Series Analysis. Sci. Total Environ. 2020, 728, 138778. "),
            html.P(html.A('•Link', href="https://doi.org/10.1016/j.scitotenv.2020.138778",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px'}),
            html.Br(),

            html.Br(),
            html.Span(
                "•  Wang, J.; Tang, K.; Feng, K.; Lv, W. High Temperature and High Humidity Reduce the Transmission of COVID-19. SSRN Electron. J. 2020"),
            html.P(html.A('•Link', href="https://doi.org/10.2139/ssrn.3551767",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px'}),
            html.Br(),

            html.Br(),
            html.Span(
                "•	Pirouz, B.; Shaffiee Haghshenas, S.;  Piro, P. Investigating a Serious Challenge in the Sustainable Development Process: Analysis of Confirmed Cases of COVID-19 (New Type of Coronavirus) Through a Binary Classification Using Artificial Intelligence and Regression Analysis. Sustainability 2020, 12 (6), 2427."),
            html.P(html.A('•Link', href="https://doi.org/10.3390/su12062427",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px'}),
            html.Br(),

            html.Br(),
            html.Span(
                "•  Li, R.; Pei, S.; Chen, B.; Song, Y.; Zhang, T.; Yang, W.; Shaman, J. Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV-2). Science 2020, 368 (6490), 489–493."),
            html.P(html.A('•Link', href="https://doi.org/10.1126/science.abb3221",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px'}),
            html.Br(),

            html.Br(),
            html.Span(
                "•  Price, R. H. M.; Graham, C.; Ramalingam, S. Association between Viral Seasonality and Meteorological Factors. Sci. Rep. 2019, 9 (1), 929."),
            html.P(html.A('•Link', href="https://doi.org/10.1038/s41598-018-37481-y",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px', 'fontColor': 'blue'}),
            html.Br(),

            html.Br(),
            html.Span(
                "•  Park, J.; Son, W.; Ryu, Y.; Choi, S. B.; Kwon, O.; Ahn, I. Effects of Temperature, Humidity, and Diurnal Temperature Range on Influenza Incidence in a Temperate Region. Influenza Other Respir. Viruses 2020, 14 (1), 11–18. "),
            html.P(html.A('•Link', href="https://doi.org/10.1111/irv.12682",
                          style={'color': '#0060FF', 'font-weight': 'bold'}),
                   style={"marginLeft": '15px', 'fontColor': 'blue'}),
            html.Br()

        ], style={"marginTop": 15}),

            width={"size": 7, "offset": 1}
        ), dbc.Col(
            html.Div(children=[
                html.Br(),
                html.Br(),
                html.H4("Contact us"),
                html.P("michaleschristodoulakes@gmail.com", style={'color': '#0060FF', 'font-weight': 'bold'}),
                html.Br(),
                html.H4("Questionnaire"),
                html.A("Google questionnaire",
                       href='https://docs.google.com/forms/d/16xwHH3wjpTRK1frYKoTaKzs7RCWX61HcH6_0wEPX1tU/edit?ts=5ebfc188#responses',
                       style={'color': '#0060FF', 'font-weight': 'bold'}),
                html.Br(),
                html.Br(),
                html.H4("Code"),
                html.A("Github repository", href='https://github.com/orestistheo/Covid19_copernicus',
                       style={'color': '#0060FF', 'font-weight': 'bold'})
            ]),
            width={"size": 3}

        )
    ]
    ),
])

about_layout = html.Div([
    header,
    dbc.Tabs([
        dbc.Tab(tab1_content, label="Participants", style={"marginLeft": "20px"}),
        dbc.Tab(tab2_content, label="References", style={"marginLeft": "20px"})
    ]
    ), footer
])

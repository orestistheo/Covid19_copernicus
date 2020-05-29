import datetime

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

mapbox_access_token = 'pk.eyJ1Ijoib3Jlc3Rpc3RoZW8iLCJhIjoiY2thY3RoMTRjMWswZTJzcDR0eTR4em9tbyJ9.DzDDLeBnKubm257RKFU1XQ'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# the dataframe  contains the association between city code and coordinates lat, lon
# column structure CityCode, Lat, Lon
coordinates = pd.read_csv(
    'C:/developmentFiles/spainCitiesCoords2.csv'
    , encoding="ISO-8859-1"
    , error_bad_lines=False)
site_lat = coordinates['Lat'] = coordinates['Lat'].astype(float)
site_lon = coordinates['Lon'] = coordinates['Lon'].astype(float)
locations_name = coordinates['CityCode'] = coordinates['CityCode'].astype(str)

# main dataframe that contains R values per city
# Ideally should have a column structure of 
#  CityCode, Date, R value, Temperature, Humidity, Maybe other climatic parameters...
data = pd.read_csv(
    'C:/developmentFiles/agregados.csv'
    , encoding="ISO-8859-1"
    , error_bad_lines=False)
Columns = ['City', 'Date', 'Nan', 'Total Cases', 'Nan', 'Nan', 'Nan', 'Deaths', 'Recovered']
data.columns = Columns
del data['Nan']
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%d/%m/%Y')
data['Date'] = pd.to_datetime(data['Date'])
data.iloc[:17, 3:5] = 0
data.iloc[17, 4] = 0
data.fillna(0, inplace=True)

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
IntroText = "Recently published papers have suggested that, as happens with the diffusion of other viruses, " \
            "air temperature and humidity could alter the spread of COVID-19. Papers in discussion also suggest " \
            "that air pollution, particularly fine particulate matter, could be involved in the morbidity and mortality due to " \
            "COVID-19 and might also play a role in spreading the SARS-CoV-2 virus. This application, provided by the Copernicus Climate Change Service," \
            " allows the user to explore some of these claims by plotting the average air temperature and humidity of the most recent months, alongside " \
            "climatological air pollution levels from the Copernicus Atmosphere Monitoring Service and the mortality data obtained from Johns Hopkins " \
            "University."

# Create the map component
fig = go.Figure()

fig.add_trace(go.Scattermapbox(
    lat=site_lat,
    lon=site_lon,
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=15,
        color='rgb(255, 0, 0)',
        opacity=0.7
    ),
    text=locations_name,
    hoverinfo='text'
))

fig.update_layout(
    title='COVID 19 prediction map',
    autosize=True,
    hovermode='closest',
    width=700,
    height=700,
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=41.390205,
            lon=2.154007,
        ),
        pitch=0,
        zoom=4,
        style='light'
    ),
)
# App Instance
app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.LUX])
# App component containing all html elements and custom style
app.layout = html.Div([
    html.Div([
        # Header component
        # Navbar
        dbc.Nav(className="nav nav-pills", children=[
            ## logo/home
            dbc.NavItem(html.Img(src=PLOTLY_LOGO, height="40px")),
            ## about
            dbc.NavItem(html.Div([
                dbc.NavLink("About", href="/", id="about-popover", active=False),
                dbc.Popover(id="about", is_open=False, target="about-popover", children=[
                    dbc.PopoverHeader("How it works")
                ])
            ])),
            ## links
            dbc.DropdownMenu(label="Links", nav=True, children=[
                dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"), "  Contacts"],
                                     target="_blank"),
                dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], target="_blank")
            ])
        ], style={"backgroundColor": "#00FFFF"})
    ]
    ),
    html.Div([
        html.Div([
            # Map component
            html.Span(IntroText, style={'marginLeft': '20px', 'font-size': '12px'})],
            style={'marginLeft': '20px', 'marginTop': '20px', 'width': '100%', 'padding-left': '12%',
                   'padding-right': '20%'}),
        html.Div([
            # Map component
            dcc.Graph(
                id='worldMapId',
                figure=fig)],
            className="six columns"),
        html.Div([
            # Diagram component
            dcc.Graph(
                style={'margin-top': '110px'},
                id='life-exp-vs-gdp',
                figure={
                    'data': [
                        dict(
                            x=data[(data['City'] == 'MD')]['Date'],
                            y=data[(data['City'] == 'MD')]['Total Cases'],
                            text='fr',
                            mode='markers+lines',
                            opacity=0.7,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'black'}
                            },
                            name='i'
                        )
                    ],
                    'layout': dict(
                        xaxis={
                            'title': 'time',
                            'type': 'date',
                            'tickmode': 'linear',
                            'dtick': 86400000.0 * 14
                        },
                        yaxis={
                            'title': 'COVID-19 cases',
                            'type': 'linear'
                        },
                        margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
                        width=400,
                        height=400,
                        hovermode='closest',
                        cursor='pointer'
                    )
                })],
            className="six columns")
    ], className="row")
])


# This function is called every time the user clicks on a point
# It returns a new figure based on the stats of the city the user has selected
@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    [Input('worldMapId', 'clickData')])
def display_click_data(clickData):
    if clickData is not None:
        filtered = coordinates[
            (coordinates['Lat'] == float(clickData['points'][0]['lat'])) &
            (coordinates['Lon'] == float(clickData['points'][0]['lon']))]
        countrycode = filtered.iat[0, 0]
        return {
            'data': [dict(
                x=data[(data['City'] == str(countrycode))]['Date'],
                y=data[(data['City'] == str(countrycode))]['Total Cases'],
                text=1,
                customdata=1,
                mode='markers',
                hoverinfo=countrycode,
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': dict(
                title=coordinates[(coordinates['CityCode'] == countrycode)]['CityName'].values[0],
                plot_bgcolor='white',
                xaxis={
                    'title': 'time',
                    'type': 'date',
                    'tickmode': 'linear',
                    'dtick': 86400000.0 * 14
                },
                yaxis={
                    'title': 'COVID-19 cases',
                    'type': 'linear'
                },
                width=400,
                height=400,
                margin={'l': 40, 'b': 30, 't': 45, 'r': 0},
                hovermode='closest'
            )
        }
    else:
        return {
            'data': [dict(
                x=0,
                y=0,
                text=1,
                customdata=1,
                mode='markers',
                hoverinfo="None",
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': dict(
                xaxis={
                    'title': 'Time'
                },
                yaxis={
                    'title': 'COVID-19 cases',
                    'type': 'linear'
                },
                width=400,
                height=400,
                margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
                hovermode='closest'
            )
        }


# # Python function to render output panel
# @app.callback(output=Output("output-panel", "children"), inputs=[Input("country", "value")])
# def render_output_panel(country):
#     data.process_data(country)
#     model = Model(data.dtf)
#     model.forecast()
#     model.add_deaths(data.mortality)
#     result = Result(model.dtf)
#     peak_day, num_max, total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days = result.get_panel()
#     peak_color = "white" if model.today > peak_day else "red"
#     panel = html.Div([
#         html.H4(country),
#         dbc.Card(body=True, className="text-white bg-primary", children=[
#             html.H6("Total cases until today:", style={"color": "white"}),
#             html.H3("{:,.0f}".format(total_cases_until_today), style={"color": "white"}),
#
#             html.H6("Total cases in 30 days:", className="text-danger"),
#             html.H3("{:,.0f}".format(total_cases_in_30days), className="text-danger"),
#
#             html.H6("Active cases today:", style={"color": "white"}),
#             html.H3("{:,.0f}".format(active_cases_today), style={"color": "white"}),
#
#             html.H6("Active cases in 30 days:", className="text-danger"),
#             html.H3("{:,.0f}".format(active_cases_in_30days), className="text-danger"),
#
#             html.H6("Peak day:", style={"color": peak_color}),
#             html.H3(peak_day.strftime("%Y-%m-%d"), style={"color": peak_color}),
#             html.H6("with {:,.0f} cases".format(num_max), style={"color": peak_color})
#
#         ])
#     ])
#     return panel


def get_panel(self):
    peak_day, num_max = self.calculate_peak(self.dtf)
    total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days = self.calculate_max(
        self.dtf)
    return peak_day, num_max, total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days


def calculate_peak(dtf):
    data_max = dtf["delta_data"].max()
    forecast_max = dtf["delta_forecast"].max()
    if data_max >= forecast_max:
        peak_day = dtf[dtf["delta_data"] == data_max].index[0]
        return peak_day, data_max
    else:
        peak_day = dtf[dtf["delta_forecast"] == forecast_max].index[0]
        return peak_day, forecast_max


def calculate_max(dtf):
    total_cases_until_today = dtf["data"].max()
    total_cases_in_30days = dtf["forecast"].max()
    active_cases_today = dtf["delta_data"].max()
    active_cases_in_30days = dtf["delta_forecast"].max()
    return total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days


app.run_server(debug=True)

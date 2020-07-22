import dash_core_components as dcc
import dash_html_components as html
import os
import pandas as pd
import plotly.graph_objects as go
import configparser
from app import app
import plotly.tools as tls
from app_components import header, footer
import dbConnection as dbConn

# Get properties for integration with external API
this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, 'ConfigFile.properties')
config = configparser.RawConfigParser()
config.read(init_file)
mapbox_access_token = config.get('ScatterMap', 'map_key')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
IntroText = "Recently published papers have suggested that, as happens with the diffusion of other viruses, " \
            "air temperature and humidity could alter the spread of COVID-19. Papers in discussion also suggest " \
            "that air pollution, particularly fine particulate matter, could be involved in the morbidity and mortality due to " \
            "COVID-19 and might also play a role in spreading the SARS-CoV-2 virus. This application, provided by the Copernicus Hackathon 2020 covid6gang team," \
            " allows the user to explore some of these claims by plotting the average air temperature, UV radiation and humidity of the most recent months, alongside " \
            "climatological air pollution levels from the Copernicus Atmosphere Monitoring Service and the mortality data obtained from Johns Hopkins " \
            "University."


# script.py
current_file = os.path.abspath(os.path.dirname(__file__))
#csv_filename
agregados_filename = os.path.join(current_file, 'agregados.csv')
coordinates_filename = os.path.join(current_file, 'spainCitiesCoords2.csv')


# the dataframe  contains the association between city code and coordinates lat, lon
# column structure CityCode, Lat, Lon
coordinates = dbConn.read_data_from_db_table('city_coordinates')
site_lat = coordinates['LATITUDE']
site_lon = coordinates['LONGTITUDE']
locations_name = coordinates['CITY_CODE']


# main dataframe that contains R values per city
# Ideally should have a column structure of 
#  CityCode, Date, R value, Temperature, Humidity, Maybe other climatic parameters...
data = pd.read_csv(
    agregados_filename
    , encoding="ISO-8859-1"
    , error_bad_lines=False)
Columns = ['City', 'Date', 'Nan', 'Total Cases', 'Nan', 'Nan', 'Nan', 'Deaths', 'Recovered', 'R_value']
data.columns = Columns
del data['Nan']
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%d/%m/%Y')
data['Date'] = pd.to_datetime(data['Date'])
data['R_value'] = data['R_value'].astype(float)
data.iloc[:17, 3:5] = 0
data.iloc[17, 4] = 0
data.fillna(0, inplace=True)

# Create the map component
fig = go.Figure()

scatter = go.Scattermapbox(
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
)

fig = go.Figure(data=[scatter])

fig.update_layout(
    title='COVID 19 prediction map',
    autosize=True,
    hovermode='closest',
    width=700,
    height=900,
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

# App component containing all html elements and custom style
map_layout = html.Div([
    header,
    html.Div([
        html.Div([
            # Map component
            html.Span(IntroText, style={'marginLeft': '20px', 'fontSize': '12px'})],
            style={'marginLeft': '20px', 'marginTop': '20px', 'width': '100%', 'paddingLeft': '12%',
                   'paddingRight': '20%'}),
        html.Div([
            # Map component
            dcc.Graph(
                id='worldMapId',
                figure=fig)],
            className="six columns"),
        html.Div([
            # Diagram component
            dcc.Graph(
                style={'marginTop': '60px'},
                id='life-exp-vs-gdp'), html.Div(id="output-panel", style=
            {"width": '300px', "height": '300px', 'marginTop': '20px', 'align': 'center', 'marginLeft': '130px'})],
            className="six columns")
    ], className="row")
    , footer
])

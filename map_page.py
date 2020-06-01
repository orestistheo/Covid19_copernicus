import dash_core_components as dcc
import dash_html_components as html
import os
import pandas as pd
import plotly.graph_objects as go
from app import app
from app_components import header, footer

mapbox_access_token = 'pk.eyJ1Ijoib3Jlc3Rpc3RoZW8iLCJhIjoiY2thd2Vud2ljMTlvYTJ4cHRnd3Bybm5haiJ9.k63ds2sBjA-kPGInervhZw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
IntroText = "Recently published papers have suggested that, as happens with the diffusion of other viruses, " \
            "air temperature and humidity could alter the spread of COVID-19. Papers in discussion also suggest " \
            "that air pollution, particularly fine particulate matter, could be involved in the morbidity and mortality due to " \
            "COVID-19 and might also play a role in spreading the SARS-CoV-2 virus. This application, provided by the Copernicus Climate Change Service," \
            " allows the user to explore some of these claims by plotting the average air temperature and humidity of the most recent months, alongside " \
            "climatological air pollution levels from the Copernicus Atmosphere Monitoring Service and the mortality data obtained from Johns Hopkins " \
            "University."


# script.py
current_file = os.path.abspath(os.path.dirname(__file__)) #older/folder2/scripts_folder
#csv_filename
agregados_filename = os.path.join(current_file, 'agregados.csv')
coordinates_filename = os.path.join(current_file, 'spainCitiesCoords2.csv')


# the dataframe  contains the association between city code and coordinates lat, lon
# column structure CityCode, Lat, Lon
coordinates = pd.read_csv(
    coordinates_filename
    , encoding="ISO-8859-1"
    , error_bad_lines=False)
site_lat = coordinates['Lat'] = coordinates['Lat'].astype(float)
site_lon = coordinates['Lon'] = coordinates['Lon'].astype(float)
locations_name = coordinates['CityCode'] = coordinates['CityCode'].astype(str)


# main dataframe that contains R values per city
# Ideally should have a column structure of 
#  CityCode, Date, R value, Temperature, Humidity, Maybe other climatic parameters...
data = pd.read_csv(
    agregados_filename
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

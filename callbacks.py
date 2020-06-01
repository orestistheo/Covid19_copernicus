from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app
from map_page import coordinates, data
import datetime


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
                mode='markers+lines',
                hoverinfo=countrycode,
                marker={
                    'size': 10,
                    'opacity': 0.5,
                    'color': 'black',
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': dict(
                title=dict(
                    text=coordinates[(coordinates['CityCode'] == countrycode)]['CityName'].values[0],
                    font=dict(
                        family="Georgia, serif",
                        size=28,
                        color="#7f7f7f"
                    ),
                    size=12,
                    color="#7f7f7f"
                ),
                plot_bgcolor='#F0F8FF',
                xaxis={
                    'type': 'date',
                    'tickmode': 'linear',
                    'dtick': 86400000.0 * 14,
                },
                yaxis={
                    'title': 'COVID-19 cases',
                    'type': 'linear'
                },
                font=dict(
                    family="Georgia, serif",
                    size=12,
                    color="#7f7f7f"
                ),
                width=600,
                height=400,
                margin={'l': 40, 'b': 40, 't': 45, 'r': 0},
                hovermode='closest'
            )
        }
    else:
        return {
            'data': [dict(
                x=1,
                y=1,
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
                plot_bgcolor='#F0F8FF',
                xaxis={
                    'type': 'date',
                    # range to display only values within this range
                    'range': [datetime.datetime(2013, 10, 17), datetime.datetime(2013, 11, 20)]
                },
                yaxis={
                    'title': 'COVID-19 cases',
                    'type': 'linear'
                },
                font=dict(
                    family="Georgia, serif",
                    size=12,
                    color="#7f7f7f"
                ),
                width=600,
                height=400,
                margin={'l': 40, 'b': 40, 't': 45, 'r': 0},
                hovermode='closest'
            )
        }


# # Python function to render output panel
@app.callback(output=Output("output-panel", "children"), inputs=[Input('worldMapId', 'clickData')])
def render_output_panel(clickData):
    if clickData is not None:
        filtered = coordinates[
            (coordinates['Lat'] == float(clickData['points'][0]['lat'])) &
            (coordinates['Lon'] == float(clickData['points'][0]['lon']))]
        country_code = filtered.iat[0, 0]
        # calculate quick stats to display
        total_cases_array = data[(data['City'] == str(country_code))]['Total Cases']
        total_deaths_array = data[(data['City'] == str(country_code))]['Deaths']
        total_cases_until_today = total_cases_array.iloc[-1]
        total_deaths_until_today = total_deaths_array.iloc[-1]
        # calculate quick stats to display
        city_name = coordinates[(coordinates['CityCode'] == country_code)]['CityName'].values[0]
        panel = html.Div([
            dbc.Card(body=True, className="text-white bg-primary", children=[
                html.H6("Total cases until today:", style={"color": "white"}),
                html.H3("{:,.0f}".format(total_cases_until_today), style={"color": "white"}),

                html.H6("Total cases in 30 days:", className="text-danger"),
                html.H3("{:,.0f}".format(30), className="text-danger"),

                html.H6("Total deaths until today:", style={"color": "white"}),
                html.H3("{:,.0f}".format(total_deaths_until_today), style={"color": "white"}),

                html.H6("Total deaths in 30 days:", className="text-danger"),
                html.H3("{:,.0f}".format(54), className="text-danger"),

                html.H6("Peak day:", style={"color": 54}),
                # html.H3(peak_day.strftime("%Y-%m-%d"), style={"color": 54}),
                html.H6("with {:,.0f} cases".format(54), style={"color": 54})

            ])
        ])
        return panel
    else:
        panel = html.Div([
            dbc.Card(body=True, className="text-white bg-primary", children=[
                html.H6("Total cases until today:", style={"color": "white"}),
                html.H3("{:,.0f}".format(0), style={"color": "white"}),

                html.H6("Total cases in 30 days:", className="text-danger"),
                html.H3("{:,.0f}".format(0), className="text-danger"),

                html.H6("Active cases today:", style={"color": "white"}),
                html.H3("{:,.0f}".format(0), style={"color": "white"}),

                html.H6("Active cases in 30 days:", className="text-danger"),
                html.H3("{:,.0f}".format(0), className="text-danger"),

                html.H6("Peak day:", style={"color": 54}),
                # html.H3(peak_day.strftime("%Y-%m-%d"), style={"color": 54}),
                html.H6("with {:,.0f} cases".format(54), style={"color": 54})

            ])
        ])
        return panel


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
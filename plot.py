import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

import config

# Custom CSS styles
custom_styles = {
    'font-family': '"Quicksand", sans-serif',
    'background-color': '#f0f0f0',
    'text-align': 'center',
    'margin': '10px',
    'padding': '10px',
    'border': '1px solid #ccc',
    'border-radius': '5px'
}
# Extra CSS style sheets
external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&family=Roboto+Slab:wght@100..900&family=Space+Grotesk:wght@300..700&display=swap",
]

# Initialize Dash app
def create_app(
        distances, velocity_profile, acceleration_profile, battery_profile,
        energy_consumption_profile, solar_profile, time
    ):
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div([
        html.Div([
            html.Img(
                src='https://cfi.iitm.ac.in/assets/Agnirath-456b8655.png',
                style={
                    'height': '60px',
                    'margin-right': '10px',
                    'border': '1px solid #fe602c',
                    'border-radius': '50%',
                    'background-color': '#000000',
                }
            ),
            html.H1("Strategy Analysis Dashboard", style={'text-align': 'center', 'font-family': '"Roboto Slab", serif'}),
        ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'align-items': 'center'}),
        
        html.Div([
            # Velocity profile plot
            dcc.Graph(
                id='velocity-profile',
                figure={
                    'data': [
                        go.Scatter(x=distances, y=velocity_profile, mode='lines+markers', name='Velocity'),
                        go.Scatter(x=[min(distances), max(distances)], y=[config.MaxVelocity, config.MaxVelocity], mode='lines', name="Max Velocity", line=dict(color='red', dash='dot')),
                        go.Scatter(x=[322000, 322000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[588000, 588000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        
                        go.Scatter(x=[987000, 987000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1210000, 1210000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1493000, 1493000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1766000, 1766000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2178000, 2178000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2432000, 2432000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2720000, 2720000], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[max(distances), max(distances)], y=[0, config.MaxVelocity], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                    ],
                    'layout': go.Layout(title='Velocity Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Velocity'})
                },
                style={'width': '93%', 'display': 'inline-block', 'vertical-align': 'top', **custom_styles}
            ),

            # Textual summary next to velocity profile
            html.Div([
                html.H2("Summary", style={'text-align': 'center', 'font-family': '"Space Grotesk", sans-serif'}),
                html.P(f"Total Distance: {round(distances[-1]/1000, 3)} km"),
                html.P(f"Time Taken: {time[-1]//3600}hrs {(time[-1]%3600)//60}mins {round(((time[-1]%3600)%60), 3)}secs"),
                html.P(f"No of points: {len(distances)}pts"),

            ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top', 'padding-left': '20px', **custom_styles}),
            
            # Textual summary next to velocity profile
            html.Div([
                html.H2("Data Analysis",
                        style={'text-align': 'center', 'font-family': '"Space Grotesk", sans-serif',
                               'margin-bottom': 0}),
                html.Div([
                    html.Div([
                        html.P(f"Max Velocity: {round(max(velocity_profile), 3)} m/s"),
                        html.P(f"Avg Velocity: {round(sum(velocity_profile)/len(velocity_profile), 3)} m/s"),
                    ], style={'width': '50%'}),
                    html.Div([
                        html.P(f"Average Battery Level: {sum(battery_profile)/len(battery_profile):.2f}%")
                    ], style={'width': '50%'})
                ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'})
            ], style={'width': '65%', 'display': 'inline-block', 'vertical-align': 'top', 'padding-left': '20px', **custom_styles}),
        ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),

        # Grid layout for other profiles
        html.Div([
            dcc.Graph(
                id='acceleration-profile',
                figure={
                    'data': [go.Scatter(x=distances[1:], y=acceleration_profile[1:], mode='lines+markers', name='Acceleration')],
                    'layout': go.Layout(title='Acceleration Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Acceleration'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='battery-profile',
                figure={
                    'data': [
                        go.Scatter(x=distances, y=battery_profile, mode='lines+markers', name='Battery'),
                        go.Scatter(x=[min(distances), max(distances)], y=[100, 100], mode='lines', name="Max Battery Level", line=dict(color='red', dash='dot')),
                        go.Scatter(x=[min(distances), max(distances)], y=[config.DeepDischargeCap*100, config.DeepDischargeCap*100], mode='lines', name="Minimum battery Level", line=dict(color='orange', dash='dot')),
                        go.Scatter(x=[322000, 322000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[588000, 588000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[987000, 987000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1210000, 1210000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1493000, 1493000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1766000, 1766000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2178000, 2178000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2432000, 2432000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2720000, 2720000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                    ],
                    'layout': go.Layout(title='Battery Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Battery Level'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='energy-consumption-profile',
                figure={
                    'data': [go.Scatter(x=distances[1:], y=energy_consumption_profile[1:], mode='lines+markers', name='Energy Consumption')],
                    'layout': go.Layout(title='Energy Consumption Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Energy Consumption'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='solar-profile',
                figure={
                    'data': [go.Scatter(x=distances[1:], y=solar_profile[1:], mode='lines+markers', name='Solar')],
                    'layout': go.Layout(title='Solar Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Solar Energy'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='net-energy-consumption-profile',
                figure={
                    'data': [go.Scatter(x=distances[1:], y=energy_consumption_profile[1:].cumsum(), mode='lines+markers', name='Energy Consumption')],
                    'layout': go.Layout(title='Net Energy Consumption Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Energy Consumption'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='net-solar-profile',
                figure={
                    'data': [go.Scatter(x=distances[1:], y=solar_profile[1:].cumsum(), mode='lines+markers', name='Solar')],
                    'layout': go.Layout(title='Net Solar Profile', xaxis={'title': 'Distance'}, yaxis={'title': 'Solar Energy'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
            dcc.Graph(
                id='time-profile',
                figure={
                    'data': [
                        go.Scatter(x=distances, y=time/3600, mode='lines+markers', name='Time'),
                        go.Scatter(x=[322000, 322000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[588000, 588000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[987000, 987000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1210000, 1210000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1493000, 1493000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[1766000, 1766000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2178000, 2178000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2432000, 2432000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                        go.Scatter(x=[2720000, 2720000], y=[0, 100], mode='lines', name="ControlStop", line=dict(color='blue', dash='dot')),
                    ],
                    'layout': go.Layout(title='Time Distance Correlation', xaxis={'title': 'Distance'}, yaxis={'title': 'Net Time'})
                },
                style={'width': '45%', 'display': 'inline-block', **custom_styles}
            ),
        ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'})
    ], style={'background-color': '#ffffff', 'padding': '20px'})

    return app

if __name__ == '__main__':
    output = pd.read_csv("run_dat.csv").fillna(0)
    distances, velocity_profile, acceleration_profile, battery_profile, energy_consumption_profile, solar_profile, time = map(np.array, (output[c] for c in output.columns.to_list()))

    distances = distances.cumsum()
    # time = time.cumsum()

    app = create_app(
        distances, velocity_profile, acceleration_profile, battery_profile,
        energy_consumption_profile, solar_profile, time
    )
    app.run_server(debug=True)

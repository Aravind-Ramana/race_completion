import dash
# from dash import dcc, html
# import plotly.graph_objs as go
# import pandas as pd
# import numpy as np

# # Custom CSS styles
# custom_styles = {
#     'font-family': '"Quicksand", sans-serif',
#     'background-color': '#f0f0f0',
#     'text-align': 'center',
#     'margin': '10px',
#     'padding': '10px',
#     'border': '1px solid #ccc',
#     'border-radius': '5px'
# }
# # Extra CSS style sheets
# external_stylesheets = [
#     "https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&family=Roboto+Slab:wght@100..900&family=Space+Grotesk:wght@300..700&display=swap",
# ]

# # Initialize Dash app
# def create_app(
#         distances, velocity_profile, acceleration_profile, battery_profile,
#         energy_consumption_profile, solar_profile, time
#     ):
#     app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#     # Calculate the derivative of the energy consumption profile and scale it
#     energy_consumption_derivative_scaled = abs(np.gradient(energy_consumption_profile) / 3055)

#     # Define the intervals
#     intervals = [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4)]

#     # Classify the scaled derivative values into intervals
#     interval_classification = np.digitize(energy_consumption_derivative_scaled, [interval[1] for interval in intervals])

#     # Calculate the time spent in each interval
#     dt = time[1] - time[0]
#     interval_times = []
#     for i, interval in enumerate(intervals):
#         points_in_interval = np.sum(interval_classification == (i + 1))
#         time_spent = points_in_interval * dt
#         interval_times.append((interval, time_spent))

#     app.layout = html.Div([
#         # Your existing layout code...
#         # Add a new div to display interval times
#         html.Div([
#             html.H2("Time Spent in Each Interval", style={'text-align': 'center', 'font-family': '"Space Grotesk", sans-serif'}),
#             html.Ul([html.Li(f"Interval {interval}: {time_spent} seconds") for interval, time_spent in interval_times])
#         ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top', 'padding-left': '20px', **custom_styles}),
#         # Your existing layout code...
#     ], style={'background-color': '#ffffff', 'padding': '20px'})

#     return app

# if __name__ == '__main__':
#     output = pd.read_csv("run_dat.csv")
#     distances, velocity_profile, acceleration_profile, battery_profile, energy_consumption_profile, solar_profile, time = map(np.array, (output[c] for c in output.columns.to_list()))

#     distances = distances.cumsum()

#     app = create_app(
#         distances, velocity_profile, acceleration_profile, battery_profile,
#         energy_consumption_profile, solar_profile, time
#     )
#     app.run_server(debug=True)

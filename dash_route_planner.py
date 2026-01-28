"""
Ship Route Planner - Dash/Plotly Version

A web-based application for planning oceanographic research cruise routes
with interactive maps and automatic time calculations.

Requirements:
    pip install dash plotly pandas dash-leaflet

Run:
    python dash_route_planner.py
    
Then open: http://127.0.0.1:8050
"""

import dash
from dash import dcc, html, Input, Output, State, ALL, ctx, callback
import dash_leaflet as dl
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import json
import math
from io import StringIO

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Ship Route Planner"

# Default route data
DEFAULT_ROUTE = [
    {
        'id': 1,
        'stationId': 'Station-1',
        'lat': 40.7128,
        'lng': -74.0060,
        'distance': 0,
        'speed': 8,
        'arrival': '',
        'departure': '2026-01-24 09:00',
        'duration': 0,
        'comments': 'Starting point'
    },
    {
        'id': 2,
        'stationId': 'Station-2',
        'lat': 40.6955,
        'lng': -73.9751,
        'distance': 8.5,
        'speed': 8,
        'arrival': '2026-01-24 09:10',
        'departure': '2026-01-24 09:15',
        'duration': 0,
        'comments': 'Midpoint'
    },
    {
        'id': 3,
        'stationId': 'Station-3',
        'lat': 40.6782,
        'lng': -73.9442,
        'distance': 17.2,
        'speed': 8,
        'arrival': '2026-01-24 09:30',
        'departure': '',
        'duration': 0,
        'comments': 'Destination'
    }
]


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points in nautical miles using Haversine formula"""
    R = 3440.065  # Earth's radius in nautical miles
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c


def update_distances(route_data):
    """Update cumulative distances for all stations"""
    cumulative = 0
    for i, station in enumerate(route_data):
        if i == 0:
            station['distance'] = 0
        else:
            prev = route_data[i-1]
            dist = calculate_distance(prev['lat'], prev['lng'], station['lat'], station['lng'])
            cumulative += dist
            station['distance'] = round(cumulative, 2)
    return route_data


def calculate_times(route_data):
    """Calculate arrival and departure times based on speed, distance, and duration"""
    for i, station in enumerate(route_data):
        if i == 0:
            station['arrival'] = ''
        else:
            prev = route_data[i-1]
            if prev['departure']:
                segment_distance = station['distance'] - prev['distance']
                speed = station['speed'] if station['speed'] > 0 else prev['speed']
                
                if speed > 0:
                    travel_hours = segment_distance / speed
                    prev_departure = datetime.fromisoformat(prev['departure'].replace(' ', 'T'))
                    arrival = prev_departure + timedelta(hours=travel_hours)
                    station['arrival'] = arrival.strftime('%Y-%m-%d %H:%M')
                    
                    duration_hours = station['duration']
                    departure = arrival + timedelta(hours=duration_hours)
                    station['departure'] = departure.strftime('%Y-%m-%d %H:%M')
    
    # Last station has no departure
    if route_data:
        route_data[-1]['departure'] = ''
    
    return route_data


def create_map(route_data):
    """Create Dash Leaflet map with route"""
    # Create markers
    markers = []
    for i, station in enumerate(route_data):
        is_start_end = (i == 0 or i == len(route_data) - 1)
        color = 'red' if is_start_end else 'blue'
        
        markers.append(
            dl.CircleMarker(
                center=[station['lat'], station['lng']],
                radius=8,
                color='white',
                fillColor=color,
                fillOpacity=1,
                weight=2,
                id={'type': 'marker', 'index': i}
            )
        )
    
    # Create polyline
    positions = [[s['lat'], s['lng']] for s in route_data]
    polyline = dl.Polyline(positions=positions, color='#3388ff', weight=4, opacity=0.7)
    
    # Calculate map center and bounds
    lats = [s['lat'] for s in route_data]
    lngs = [s['lng'] for s in route_data]
    center = [sum(lats)/len(lats), sum(lngs)/len(lngs)]
    
    return dl.Map(
        id='route-map',
        center=center,
        zoom=10,
        children=[
            dl.TileLayer(),
            polyline,
            *markers
        ],
        style={'width': '100%', 'height': '600px'}
    )


def create_table(route_data):
    """Create editable table with route data"""
    return html.Div([
        html.Table([
            # Header
            html.Thead(html.Tr([
                html.Th('Station'),
                html.Th('Lat (decimal)'),
                html.Th('Lon (decimal)'),
                html.Th('Dist (nm)'),
                html.Th('Spd (kn)'),
                html.Th('Arrival'),
                html.Th('Departure'),
                html.Th('On Stn (hrs)'),
                html.Th('Comments'),
            ], style={'backgroundColor': '#2c5aa0', 'color': 'white'})),
            
            # Body
            html.Tbody([
                html.Tr([
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'stationId', 'index': i},
                        value=station['stationId'],
                        style={'width': '100%'}
                    )),
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'lat', 'index': i},
                        type='number',
                        value=station['lat'],
                        step=0.000001,
                        style={'width': '100%'}
                    )),
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'lng', 'index': i},
                        type='number',
                        value=station['lng'],
                        step=0.000001,
                        style={'width': '100%'}
                    )),
                    html.Td(f"{station['distance']:.2f}", style={'backgroundColor': '#f8f9fa'}),
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'speed', 'index': i},
                        type='number',
                        value=station['speed'],
                        step=0.1,
                        style={'width': '100%'}
                    )),
                    html.Td(
                        dcc.Input(
                            id={'type': 'station-input', 'field': 'arrival', 'index': i},
                            type='text',
                            value=station['arrival'],
                            disabled=(i == 0),
                            style={'width': '100%'}
                        ) if i > 0 else ''
                    ),
                    html.Td(
                        dcc.Input(
                            id={'type': 'station-input', 'field': 'departure', 'index': i},
                            type='text',
                            value=station['departure'],
                            disabled=(i == len(route_data) - 1),
                            style={'width': '100%'}
                        ) if i < len(route_data) - 1 else ''
                    ),
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'duration', 'index': i},
                        type='number',
                        value=station['duration'],
                        step=0.1,
                        style={'width': '100%'}
                    )),
                    html.Td(dcc.Input(
                        id={'type': 'station-input', 'field': 'comments', 'index': i},
                        value=station['comments'],
                        style={'width': '100%'}
                    )),
                ], style={'backgroundColor': '#ffffff' if i % 2 == 0 else '#e7f3ff'})
                for i, station in enumerate(route_data)
            ])
        ], style={'width': '100%', 'borderCollapse': 'collapse'})
    ])


# App layout
app.layout = html.Div([
    html.H1('Ship Route Planner', style={'textAlign': 'center', 'color': '#2c5aa0'}),
    
    # Store for route data
    dcc.Store(id='route-store', data=DEFAULT_ROUTE),
    
    # Control panel
    html.Div([
        html.Div([
            html.Label('Default Ship Speed (knots): '),
            dcc.Input(id='default-speed', type='number', value=8, step=0.1, min=0, style={'marginLeft': '10px', 'marginRight': '10px'}),
            html.Button('Apply to All', id='apply-speed-btn', style={'backgroundColor': '#2c5aa0', 'color': 'white', 'border': 'none', 'padding': '5px 15px', 'cursor': 'pointer'}),
        ], style={'padding': '15px', 'backgroundColor': '#2c5aa0', 'color': 'white'}),
        
        html.Div([
            html.Button('Download CSV', id='download-csv-btn', style={'margin': '5px', 'backgroundColor': '#28a745', 'color': 'white', 'border': 'none', 'padding': '8px 15px', 'cursor': 'pointer'}),
            html.Button('Download GeoJSON', id='download-geojson-btn', style={'margin': '5px', 'backgroundColor': '#6f42c1', 'color': 'white', 'border': 'none', 'padding': '8px 15px', 'cursor': 'pointer'}),
            dcc.Upload(
                id='upload-csv',
                children=html.Button('Upload CSV', style={'margin': '5px', 'backgroundColor': '#17a2b8', 'color': 'white', 'border': 'none', 'padding': '8px 15px', 'cursor': 'pointer'}),
                multiple=False
            ),
            html.Button('Reset', id='reset-btn', style={'margin': '5px', 'backgroundColor': '#dc3545', 'color': 'white', 'border': 'none', 'padding': '8px 15px', 'cursor': 'pointer'}),
        ], style={'padding': '10px', 'textAlign': 'center', 'backgroundColor': '#f8f9fa'}),
    ]),
    
    # Map
    html.Div(id='map-container', style={'padding': '20px'}),
    
    # Table
    html.Div(id='table-container', style={'padding': '20px', 'overflowX': 'auto'}),
    
    # Download components
    dcc.Download(id='download-csv'),
    dcc.Download(id='download-geojson'),
    
], style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1400px', 'margin': '0 auto'})


# Callbacks
@app.callback(
    [Output('map-container', 'children'),
     Output('table-container', 'children'),
     Output('route-store', 'data')],
    [Input('route-store', 'data'),
     Input('apply-speed-btn', 'n_clicks'),
     Input('reset-btn', 'n_clicks'),
     Input('upload-csv', 'contents'),
     Input({'type': 'station-input', 'field': ALL, 'index': ALL}, 'value')],
    [State('default-speed', 'value'),
     State('upload-csv', 'filename'),
     State({'type': 'station-input', 'field': ALL, 'index': ALL}, 'id')]
)
def update_route(route_data, apply_clicks, reset_clicks, upload_contents, input_values, default_speed, upload_filename, input_ids):
    """Main callback to update route data and UI"""
    
    triggered = ctx.triggered_id
    
    # Handle reset
    if triggered == 'reset-btn' and reset_clicks:
        route_data = DEFAULT_ROUTE.copy()
    
    # Handle CSV upload
    elif triggered == 'upload-csv' and upload_contents:
        try:
            content_type, content_string = upload_contents.split(',')
            import base64
            decoded = base64.b64decode(content_string).decode('utf-8')
            df = pd.read_csv(StringIO(decoded))
            
            route_data = []
            for i, row in df.iterrows():
                route_data.append({
                    'id': i + 1,
                    'stationId': row['Station ID'],
                    'lat': float(row['Latitude']),
                    'lng': float(row['Longitude']),
                    'distance': float(row['Distance (nm)']),
                    'speed': float(row['Speed (knots)']),
                    'arrival': row['Arrival'],
                    'departure': row['Departure'],
                    'duration': float(row['Duration (hrs)']),
                    'comments': row['Comments'] if pd.notna(row['Comments']) else ''
                })
        except Exception as e:
            print(f"Error uploading CSV: {e}")
    
    # Handle apply speed to all
    elif triggered == 'apply-speed-btn' and apply_clicks and default_speed:
        for station in route_data:
            station['speed'] = default_speed
    
    # Handle individual input changes
    elif triggered and isinstance(triggered, dict) and triggered.get('type') == 'station-input':
        for input_id, value in zip(input_ids, input_values):
            idx = input_id['index']
            field = input_id['field']
            if idx < len(route_data):
                if field in ['lat', 'lng', 'speed', 'duration']:
                    route_data[idx][field] = float(value) if value else 0
                else:
                    route_data[idx][field] = value if value else ''
    
    # Recalculate distances and times
    route_data = update_distances(route_data)
    route_data = calculate_times(route_data)
    
    # Create map and table
    map_component = create_map(route_data)
    table_component = create_table(route_data)
    
    return map_component, table_component, route_data


@app.callback(
    Output('download-csv', 'data'),
    Input('download-csv-btn', 'n_clicks'),
    State('route-store', 'data'),
    prevent_initial_call=True
)
def download_csv(n_clicks, route_data):
    """Download route data as CSV"""
    df = pd.DataFrame([{
        'Station ID': s['stationId'],
        'Latitude': s['lat'],
        'Longitude': s['lng'],
        'Distance (nm)': s['distance'],
        'Speed (knots)': s['speed'],
        'Arrival': s['arrival'],
        'Departure': s['departure'],
        'Duration (hrs)': s['duration'],
        'Comments': s['comments']
    } for s in route_data])
    
    return dcc.send_data_frame(df.to_csv, 'route_data.csv', index=False)


@app.callback(
    Output('download-geojson', 'data'),
    Input('download-geojson-btn', 'n_clicks'),
    State('route-store', 'data'),
    prevent_initial_call=True
)
def download_geojson(n_clicks, route_data):
    """Download route data as GeoJSON"""
    geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [s['lng'], s['lat']]
            },
            "properties": {
                "name": s['stationId'],
                "arrive": s['arrival'],
                "departure": s['departure'],
                "comments": s['comments'],
                "depth": "",
                "duration": str(s['duration'])
            }
        } for s in route_data]
    }
    
    return dict(content=json.dumps(geojson, indent=2), filename='route_data.geojson')


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Ship Route Planner - Dash/Plotly Version")
    print("="*60)
    print("\nStarting server...")
    print("Open your browser to: http://127.0.0.1:8050")
    print("\nPress Ctrl+C to stop the server\n")
    
    app.run_server(debug=True, port=8050)

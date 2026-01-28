# Ship Route Planner - Dash/Plotly Version

A Python web application for planning oceanographic research cruise routes using Dash, Plotly, and Dash Leaflet.

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements_dash.txt

# Run the application
python dash_route_planner.py
```

Then open your browser to: **http://127.0.0.1:8050**

## Features

### ✅ What's Included

- **Interactive Leaflet Map**: OpenStreetMap tiles with route visualization
- **Editable Data Table**: Real-time editing of station data
- **Automatic Calculations**: Distance (Haversine formula) and time calculations
- **CSV Import/Export**: Upload existing routes or download for backup
- **GeoJSON Export**: Compatible with GIS software
- **Python Backend**: Server-side data processing
- **Apply Speed to All**: Quickly update all stations
- **Reset Function**: Return to default route

### How It Works

1. **Edit the table**: Click any input field to modify station data
2. **View updates**: Map and table update automatically
3. **Export data**: Download CSV or GeoJSON files
4. **Import routes**: Upload previously saved CSV files

## Comparison: Dash vs HTML Version

| Feature | Dash/Plotly | Standalone HTML |
|---------|-------------|-----------------|
| **Installation** | Requires Python | None - just open file |
| **Offline Use** | ❌ Needs server | ✅ Fully offline |
| **Draggable Markers** | ❌ Not implemented | ✅ Full drag support |
| **Click to Add Stations** | ❌ Not available | ✅ Click polyline |
| **Undo Functionality** | ❌ Not implemented | ✅ 50-action history |
| **Resizable Panels** | ❌ Fixed layout | ✅ Draggable divider |
| **Date/Time Pickers** | ❌ Text input only | ✅ Dropdown selectors |
| **Python Integration** | ✅ Full support | ❌ JavaScript only |
| **Database Storage** | ✅ Easy to add | ❌ LocalStorage only |
| **Multi-User** | ✅ Possible | ❌ Single user |
| **API Integration** | ✅ Easy | ❌ Limited |
| **Cloud Deployment** | ✅ Heroku, AWS, etc | ❌ Static hosting only |
| **Field Work** | ❌ Needs server | ✅ Perfect for ships |

## When to Use Dash Version

Choose Dash if you need:
- ✅ Python data science ecosystem (pandas, numpy, scipy)
- ✅ Database storage (PostgreSQL, MongoDB, etc.)
- ✅ Multi-user access with authentication
- ✅ API integrations (weather, AIS, oceanographic data)
- ✅ Cloud deployment and scaling
- ✅ Background processing and automation
- ✅ Server-side validation and security

## When to Use HTML Version

Choose standalone HTML if you need:
- ✅ **No installation** - works immediately
- ✅ **Offline use** - perfect for ships at sea
- ✅ **Better interactivity** - drag markers, undo, resize
- ✅ **Field deployment** - no dependencies
- ✅ **Quick sharing** - single file
- ✅ **More complete features** - date pickers, undo, etc.

**Recommendation**: For oceanographic field work, the **standalone HTML version is better** because it works offline and has more interactive features.

## Extending the Dash Version

### Add Database Storage

```python
import sqlite3
import pandas as pd

def save_route(route_data, route_name):
    conn = sqlite3.connect('routes.db')
    df = pd.DataFrame(route_data)
    df['route_name'] = route_name
    df.to_sql('routes', conn, if_exists='append', index=False)
    conn.close()

def load_route(route_name):
    conn = sqlite3.connect('routes.db')
    df = pd.read_sql(f"SELECT * FROM routes WHERE route_name='{route_name}'", conn)
    conn.close()
    return df.to_dict('records')
```

### Add Weather Integration

```python
import requests

@app.callback(
    Output('weather-info', 'children'),
    Input('route-store', 'data')
)
def get_weather(route_data):
    # Example: Get weather for each station
    weather_data = []
    for station in route_data:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={station['lat']}&lon={station['lng']}&appid=YOUR_API_KEY"
        )
        weather_data.append(response.json())
    return display_weather(weather_data)
```

### Add User Authentication

```python
from flask_login import LoginManager, login_required

server = app.server
login_manager = LoginManager()
login_manager.init_app(server)

# Protect routes
@server.route('/dashboard')
@login_required
def dashboard():
    return app.index()
```

### Deploy to Heroku

```bash
# Create Procfile
echo "web: gunicorn dash_route_planner:server" > Procfile

# Create runtime.txt
echo "python-3.9.18" > runtime.txt

# Deploy
git init
git add .
git commit -m "Initial commit"
heroku create my-route-planner
git push heroku main
```

## Current Limitations

The Dash version is a **simplified proof-of-concept** and lacks:

1. **Draggable markers** - Would require custom JavaScript or Dash Leaflet extensions
2. **Click polyline to add** - Complex interaction not built-in to Dash Leaflet
3. **Undo/redo** - Can be added with history management in Store
4. **Date/time pickers** - Using text inputs instead of dropdowns
5. **Resizable layout** - Fixed two-column layout
6. **Mouse coordinate display** - Not available in Dash Leaflet
7. **Setup modal** - No initial configuration wizard
8. **First/last station logic** - Arrival/departure fields not properly disabled

## Recommended Improvements

To make the Dash version production-ready:

1. **Add Dash Leaflet plugins** for marker dragging
2. **Implement undo/redo** using dcc.Store history
3. **Create setup wizard** with dcc.Modal
4. **Add date/time components** using dcc.DatePickerSingle and dropdowns
5. **Implement user authentication** with Flask-Login
6. **Add database backend** (PostgreSQL recommended)
7. **Create multi-route management** system
8. **Add export formats** (KML, GPX for GPS devices)
9. **Integrate weather** and oceanographic data APIs
10. **Add route optimization** algorithms

## Code Structure

```python
dash_route_planner.py        # Main application (500+ lines)
├── calculate_distance()      # Haversine distance calculation
├── update_distances()        # Update cumulative distances
├── calculate_times()         # Calculate arrival/departure times
├── create_map()              # Generate Dash Leaflet map
├── create_table()            # Generate editable HTML table
└── Callbacks:
    ├── update_route()        # Main callback for data updates
    ├── download_csv()        # CSV export
    └── download_geojson()    # GeoJSON export
```

## Performance Notes

- **Client-side**: All calculations happen on server, not in browser
- **Scalability**: Can handle multiple concurrent users
- **Database**: Add connection pooling for production
- **Caching**: Use `@cache.memoize()` for expensive calculations

## Conclusion

This Dash/Plotly version demonstrates how the route planner **could** work as a Python web app, but the **standalone HTML version is currently more feature-complete** and better suited for oceanographic field work.

**Use Dash if**: You need Python integration, databases, or multi-user access
**Use HTML if**: You need it to work offline on a ship (recommended!)

---

**Happy route planning!** 🚢🐍

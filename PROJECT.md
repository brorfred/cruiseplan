# Ship Route Planner

A comprehensive web-based application for planning oceanographic research cruise routes.

## Project Structure

```
ship-route-planner/
├── route_planner.html          # Standalone HTML application (recommended)
├── README.md                    # Complete user guide
├── dash_route_planner.py       # Dash/Plotly Python version
├── requirements_dash.txt       # Python dependencies for Dash version
└── README_DASH.md              # Dash version documentation and comparison
```

## Quick Start

### Option 1: Standalone HTML (Recommended for Field Work)

Simply open `route_planner.html` in any modern web browser. No installation required!

**Best for:**
- Offline use on ships
- No dependencies
- Full interactive features
- Quick deployment

### Option 2: Dash/Plotly Python App

```bash
pip install -r requirements_dash.txt
python dash_route_planner.py
```

Then open: http://127.0.0.1:8050

**Best for:**
- Python integration
- Database storage
- Multi-user access
- API integrations

## Features

### Standalone HTML Version

✅ Interactive Leaflet map with draggable markers
✅ Automatic distance and time calculations
✅ 24-hour time format with dropdown selectors
✅ ISO date format (YYYY-MM-DD)
✅ Undo functionality (50 actions)
✅ Resizable map/table panels
✅ CSV and GeoJSON export/import
✅ Mouse coordinate display
✅ LocalStorage persistence
✅ Setup modal for initialization
✅ No installation required
✅ Works offline

### Dash/Plotly Version

✅ Python backend for server-side processing
✅ Interactive Leaflet map
✅ Editable data table
✅ CSV/GeoJSON export
✅ Automatic calculations
✅ Easy database integration
✅ API integration ready
✅ Cloud deployment ready

## Documentation

- **[README.md](README.md)** - Complete user guide for HTML version
- **[README_DASH.md](README_DASH.md)** - Dash version guide and comparison

## Development History

This repository contains the complete development history with each feature as a separate commit:

1. Initial project setup
2. Basic HTML structure with map and table
3. Interactive markers and route lines
4. Distance calculations (Haversine formula)
5. Automatic time calculations
6. CSV/GeoJSON export functionality
7. Table styling and formatting improvements
8. 24-hour time format with dropdowns
9. Undo functionality
10. Resizable panels with draggable divider
11. Mouse position display
12. Setup modal with CSV upload
13. Dash/Plotly Python version

## Technology Stack

### HTML Version
- Leaflet.js - Interactive maps
- Tabulator.js - Data tables
- Vanilla JavaScript - No framework dependencies
- LocalStorage - Data persistence

### Dash Version
- Dash - Python web framework
- Plotly - Interactive visualizations
- Dash Leaflet - Map component
- Pandas - Data manipulation

## License

MIT License - Free to use and modify

## Contributing

This project was developed through an iterative process. Each commit represents a feature addition or improvement. See git history for details.

## Support

For issues or questions, refer to:
- README.md for HTML version
- README_DASH.md for Dash version

---

**Recommended**: Use the standalone HTML version (`route_planner.html`) for oceanographic field work! 🚢🗺️

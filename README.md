# Ship Route Planner

A web-based application for planning oceanographic research cruise routes with interactive maps, automatic time calculations, and data export capabilities.

## Features

- **Interactive Map**: Leaflet-based map with draggable station markers
- **Automatic Calculations**: Distance (nautical miles), arrival/departure times
- **Customizable Routes**: Add, delete, and rearrange stations
- **Data Persistence**: Routes automatically save to browser storage
- **Import/Export**: CSV and GeoJSON file support
- **Undo Functionality**: Revert up to 50 previous actions
- **24-Hour Time Format**: Professional maritime time display
- **Resizable Interface**: Adjustable map/table split view

## Getting Started

### First Time Setup

1. **Open the Application**: Open `route_planner.html` in a web browser
2. **Setup Modal**: On first load, you'll see a setup screen asking for:
   - **Start Position**: Name, Latitude, Longitude
   - **End Position**: Name, Latitude, Longitude
   - **Default Ship Speed**: Speed in knots (default: 8)
   - **Number of Stations**: Total stations including start/end (default: 3)
3. **Create Route**: Click "Create Route" to generate your initial route

### Interface Overview

The application is split into two main panels:

**Left Panel - Map**
- Interactive map showing your route
- Red markers: Start and end stations
- Blue markers: Intermediate waypoints
- Blue line: Route polyline connecting all stations
- Mouse coordinates display (bottom-left corner)

**Right Panel - Data Table**
- Station information in a two-row layout per station:
  - **Top row**: Station ID, Lat, Lon, Distance, Speed, Arrival, Departure, Duration
  - **Bottom row**: Comments field

## Working with Stations

### Adding Stations

**Click the polyline** between any two stations to insert a new waypoint at that location.
- The new station will be automatically numbered
- Default speed will be applied
- Times will recalculate automatically

### Moving Stations

**Click and drag** any station marker on the map to reposition it.
- Coordinates in the table update automatically
- Distances and times recalculate
- Action is saved to undo history

### Deleting Stations

**Right-click** any intermediate station marker (not start/end) and confirm deletion.
- Start and end stations cannot be deleted
- Station numbering updates automatically
- Times and distances recalculate

## Editing Data

### Date and Time Fields

**Arrival/Departure columns** use dropdown selectors:
- **Date**: Click to open calendar picker (ISO format: YYYY-MM-DD)
- **Hour**: Select 00-23 (24-hour format)
- **Minute**: Select 00-59

**First station**: 
- No arrival time (you start here)
- Only departure time is editable

**Subsequent stations**:
- Both arrival and departure times are editable
- Changing either will recalculate all following stations

### Other Editable Fields

- **Station ID**: Click to rename stations
- **Lat/Lon**: Edit coordinates directly (6 decimal places)
- **Speed**: Station-specific speed in knots
- **Duration (On Stn)**: Hours spent at station
- **Comments**: Click the comment row to add notes

### Automatic Calculations

The app automatically calculates:

1. **Distance**: Cumulative nautical miles from start using Haversine formula
2. **Arrival Time**: Previous departure + (segment distance / speed)
3. **Departure Time**: Arrival + duration on station

**Manual Override**: Edit any arrival/departure time to manually set it. All subsequent stations will recalculate based on your change.

## Speed Settings

### Default Speed Form (Top Bar)

- **Default Ship Spd**: Sets the default speed for new stations
- **Apply to All**: Updates all existing stations with this speed

### Station-Specific Speed

Edit individual station speeds in the "Spd" column. This allows for:
- Slower speeds in rough weather areas
- Faster transit between stations
- Variable ship performance

## Using the Undo Feature

**Undo Button** (gray button in bottom panel):
- Reverts the last change made
- Stores up to 50 actions
- Tooltip shows number of available undo actions
- Works for: marker drags, deletions, additions, all table edits, CSV imports

## Resizing the Interface

**Draggable Divider** (vertical bar between map and table):
- Hover over the divider until cursor changes to ↔
- Click and drag left/right to resize panels
- Minimum widths enforced (Map: 300px, Table: 400px)
- Map automatically adjusts after resize

## Import/Export

### Download CSV

Exports route data to spreadsheet format with columns:
- Station ID, Latitude, Longitude, Distance (nm), Speed (knots)
- Arrival, Departure, Duration (hrs), Comments

**Use for**: Excel analysis, backup, sharing with colleagues

### Download GeoJSON

Exports route as GeoJSON FeatureCollection with:
- Point features for each station
- Properties: name, arrive, departure, comments, depth, duration

**Use for**: GIS software, mapping applications, scientific analysis

### Upload CSV

Import previously exported routes or create routes from spreadsheet:
1. Click "Upload CSV"
2. Select your CSV file
3. Route will replace current data (use Undo if needed)

**CSV Format**: Must match export format with headers in first row

## Reset All Data

**Reset Button** (red button):
- Clears all data and returns to setup modal
- Requires confirmation
- Cannot be undone (data is permanently deleted)

**Use when**: Starting a completely new cruise plan

## Tips and Best Practices

### Route Planning

1. **Start with setup modal**: Define start/end points and approximate station count
2. **Adjust positions**: Drag markers to precise locations using coordinate display
3. **Set realistic speeds**: Consider weather, sea state, ship capabilities
4. **Add durations**: Include realistic on-station time for sampling/operations
5. **Use comments**: Document station purposes, sampling plans, special notes

### Time Management

- **Buffer time**: Add extra duration for weather delays, equipment issues
- **UTC time**: Consider using UTC for multi-day international cruises
- **Manual overrides**: Set specific arrival times for port calls or scheduled events

### Data Organization

- **Meaningful names**: Rename stations with location names or purposes
- **Regular exports**: Download CSV/GeoJSON backups periodically
- **Comments**: Document special requirements, sampling depth, etc.

### Efficiency

- **Undo liberally**: Don't hesitate to undo and try different configurations
- **Resize as needed**: Make table wider for detailed editing, map wider for positioning
- **Keyboard shortcuts**: Tab through table cells for quick data entry

## Technical Details

### Data Format

**Storage**: Browser localStorage (persists between sessions)

**Datetime Format**: YYYY-MM-DD HH:MM (ISO 8601 compatible)

**Coordinates**: Decimal degrees (6 decimal places ≈ 0.1 meter precision)

**Distance**: Nautical miles calculated using Haversine formula (Earth radius: 3440.065 nm)

### Browser Compatibility

- **Recommended**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Required**: JavaScript enabled, localStorage available
- **Features**: HTML5 date inputs, ES6 JavaScript support

### Limitations

- **No authentication**: Data stored locally only
- **Single route**: One route per browser/device
- **No cloud sync**: Data doesn't transfer between devices
- **Manual decimal degrees**: No DMS (degrees/minutes/seconds) input

## Troubleshooting

**Setup modal doesn't appear**
- Data already exists in localStorage
- Clear browser storage: Open console (F12), type `localStorage.clear()`, refresh page
- Or use "Reset All Data" button

**Times not calculating**
- Ensure all stations have valid speeds (> 0)
- Check that departure time is set for first station
- Verify datetime format is correct

**Map not loading**
- Check internet connection (requires map tiles)
- Ensure JavaScript is enabled
- Try refreshing the page

**Can't drag markers**
- Ensure you're clicking directly on the marker (red/blue circle)
- Try refreshing the page

**Undo not working**
- Undo only stores last 50 actions
- Some actions (like resizing) are not stored
- Reset clears undo history

## Support and Feedback

This is a standalone HTML application. All data is stored locally in your browser.

For issues or questions:
- Check this README first
- Verify browser compatibility
- Try clearing localStorage and starting fresh

## Version Information

**Current Features**:
- Interactive Leaflet map with draggable markers
- Two-row table layout with inline comments
- 24-hour time format with dropdown selectors
- ISO date format (YYYY-MM-DD)
- Undo functionality (50 actions)
- CSV and GeoJSON export/import
- Resizable map/table panels
- Mouse coordinate display
- Automatic time and distance calculations
- localStorage persistence
- Setup modal for initial configuration

---

**Enjoy planning your research cruise routes!** 🚢🗺️

# Changelog

All notable changes to the Ship Route Planner project.

## [v1.0-dash] - 2026-01-28

### Added - Dash/Plotly Version
- Python-based web application using Dash framework
- Dash Leaflet for interactive maps
- Server-side data processing with Python
- Editable data table with real-time updates
- CSV and GeoJSON export functionality
- CSV import functionality
- Apply speed to all stations feature
- Reset to default route
- Comprehensive documentation with comparison to HTML version

### Documentation
- README_DASH.md with complete usage guide
- Feature comparison table
- Extension examples (database, weather, auth)
- Deployment instructions

## [v1.0-html] - 2026-01-28

### Added - Standalone HTML Application
- Complete single-file HTML application
- Interactive Leaflet map with OpenStreetMap tiles
- Draggable station markers (red for start/end, blue for waypoints)
- Click polyline to insert new stations
- Right-click markers to delete (except start/end)
- Two-row table layout (data + comments)
- Automatic distance calculations using Haversine formula
- Automatic arrival/departure time calculations
- 24-hour time format with hour/minute dropdown selectors
- ISO date format (YYYY-MM-DD)
- Undo functionality with 50-action history
- Resizable map/table panels with draggable divider
- Mouse coordinate display (bottom-left corner)
- CSV export/import
- GeoJSON export
- Setup modal for initial configuration
  - Manual entry: start/end positions, speed, station count
  - CSV upload option
- LocalStorage data persistence
- Nautical color theme (dark blue #2c5aa0)
- Professional table styling with alternating row colors

### Features
- Station Management
  - Add stations by clicking polyline
  - Delete stations via right-click
  - Drag markers to reposition
  - Edit all fields inline
  
- Automatic Calculations
  - Cumulative nautical mile distances
  - Travel times based on speed
  - Arrival = Previous departure + travel time
  - Departure = Arrival + duration on station
  
- User Interface
  - Compact column widths (Lat/Lon: 65px, Spd: 50px)
  - Fixed-width datetime columns (205px)
  - Responsive layout
  - Professional maritime styling
  
- Data Management
  - Persistent storage in browser
  - Export to CSV for spreadsheets
  - Export to GeoJSON for GIS software
  - Import from CSV
  - Undo up to 50 actions
  
- Smart Defaults
  - First station: No arrival field (starting point)
  - Last station: No departure field (destination)
  - Default speed: 8 knots
  - Apply speed to all stations

### Documentation
- Complete README with usage instructions
- Tips and best practices
- Troubleshooting guide
- Technical specifications

## [Initial] - 2026-01-28

### Project Setup
- Git repository initialization
- Project structure
- .gitignore for Python and OS files
- PROJECT.md overview document

---

## Version Comparison

| Feature | HTML v1.0 | Dash v1.0 |
|---------|-----------|-----------|
| Installation | None | Python + pip |
| Offline Use | ✅ Yes | ❌ No (needs server) |
| Draggable Markers | ✅ Yes | ❌ No |
| Click Add Stations | ✅ Yes | ❌ No |
| Undo Functionality | ✅ Yes (50 actions) | ❌ No |
| Resizable Panels | ✅ Yes | ❌ No |
| Date/Time Pickers | ✅ Dropdowns | ❌ Text input |
| Mouse Coordinates | ✅ Yes | ❌ No |
| Python Integration | ❌ No | ✅ Yes |
| Database Ready | ❌ No | ✅ Yes |
| Multi-User | ❌ No | ✅ Yes |
| API Integration | ❌ Limited | ✅ Easy |

**Recommendation**: Use HTML version for oceanographic field work. Use Dash version if you need Python integration or multi-user deployment.

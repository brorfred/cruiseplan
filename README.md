# Ship Route Planner

A professional web-based route planning application for oceanographic cruises with modern UI, interactive mapping, and comprehensive data management.

![Version](https://img.shields.io/badge/version-2.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌊 Overview

The Ship Route Planner is a standalone HTML application designed for oceanographic researchers to plan and manage research cruise routes. It features an intuitive interface with drag-and-drop markers, automatic calculations, and multiple export formats.

## ✨ Features

### 🗺️ Interactive Mapping
- **OpenStreetMap integration** with satellite and street view layers
- **Draggable station markers** with real-time position updates
- **Switchable marker display**: Toggle between station numbers (②③④) or 2-letter IDs (AB, XY, QR)
- **ID/# toggle switch** in interface for quick marker mode switching
- **Click-to-add stations** on route polyline
- **Visual route lines** connecting all stations
- **Automatic map centering** to show entire route

### 🎨 Modern UI Design (v2.1)
- **Nautical theme** with dark blue (#2c5aa0) throughout
- **Pill-style buttons** with gradients and animations
- **Split pill buttons** for Download/Upload actions (green CSV, purple JSON)
- **Flatpickr datetime pickers** with ISO format (YYYY-MM-DD HH:MM)
- **Royal blue editable fields** (#4169e1) with no borders
- **White table background** for clean appearance
- **Borderless columns** - modern, uncluttered table design
- **Pagination** (default 20 rows) with compact dark blue footer
- **Compact Time Budget bar** - right-aligned, 30% width indicator
- **Perfect button alignment** with invisible spacers

### 🏷️ Smart Station Naming
- **Marine organism names** instead of numbers (e.g., "Huge_Shark", "Tiny_Whale")
- **10-character format**: Adjective_Organism with underscore
- **2,745 unique combinations** from marine-themed word lists
- **Automatic uniqueness** tracking to prevent duplicates
- **Fully customizable** - users can rename to anything
- **Unique 2-letter station codes** (AB, XY, QR) for permanent identification
- **Station column width**: 130px to accommodate full names + codes

### 📊 Data Management
- **Two-row table layout** with station details and comments
- **Compact columns** optimized for space efficiency:
  - Station Name (130px) with code display
  - Latitude/Longitude (65px each)
  - Distance (55px), Speed (40px), Duration (45px)
  - Arrival/Departure (135px each)
- **Inline editing** with royal blue highlights
- **Working datetime pickers** in table cells (calendar + manual entry)
- **Preserved scroll position** when dragging markers
- **No table borders** between columns for clean appearance
- **Automatic distance calculations** using Haversine formula
- **Automatic time calculations** based on speed and distance
- **Smart recalculation** - manual time entries preserved, only subsequent stations recalculated
- **Manual time management** - bold green text for manually set times with quick unselect button (✕) to revert to calculated values

### ⏱️ Time Budget Tracking
- **Cruise start/end dates** with deadline tracking
- **Real-time budget display** showing time surplus/deficit
- **Color-coded indicators**:
  - 🟢 Dark green (#1e7e34) - On time (positive budget)
  - 🔴 Dark red (#bd2130) - Behind schedule (negative budget)
- **Compact display**: 30% width, right-aligned
- **Positioned above table** for better visibility
- **Format**: "+2d 5h" or "-1d 3h" (days and hours)

### 💾 Import/Export Capabilities
- **CSV format** with complete station data including codes
- **GeoJSON format** for GIS integration
- **Upload/Download** for both formats via split pill buttons
- **Backward compatible** with old CSV format (9 columns)
- **New format supports**: 10 columns including Station Code
- **Round-trip fidelity** - export then import maintains all data

### 🔄 Advanced Features
- **Undo functionality** with complete history tracking
- **Custom station names** preserved when adding/deleting stations
- **Confirmation dialogs** for destructive actions
- **Speed templates** with "Apply to All" option
- **Resizable panels** for map and table views
- **Mouse position display** showing current coordinates
- **24-hour time format** throughout
- **Marker display toggle** - switch between numbers and IDs on the fly

### 🎯 User Experience
- **Setup modal** for initial route configuration
- **Batch operations** via Apply to All button
- **Right-click delete** on intermediate stations
- **Map popup updates** when station names change
- **Perfect button alignment** across all controls
- **Responsive design** that adapts to screen size
- **Seamless blue theme** - no visual breaks between sections

## 🚀 Getting Started

### Installation

1. **Download** the `route_planner.html` file
2. **Open** in any modern web browser (Chrome, Firefox, Safari, Edge)
3. **No server required** - runs entirely client-side

### First Use

1. Application opens with **Setup Modal**
2. Enter:
   - **Starting location** (name, latitude, longitude)
   - **Ending location** (name, latitude, longitude)
   - **Number of stations** (intermediate waypoints)
   - **Cruise dates** (start date/time and deadline)
3. Click **Create Route** to generate initial plan
4. Stations automatically named with marine organisms (e.g., "Bold_Whale", "Fast_Shark")

### Basic Workflow

1. **Adjust positions** by dragging markers on map
2. **Toggle marker display** using [ID][#] switch (default: #)
3. **Edit station details** directly in table cells
4. **Add stations** by clicking on the route line
5. **Delete stations** by right-clicking markers (except start/end)
6. **Set times** using datetime pickers (calendar or manual entry)
7. **Rename stations** by clicking the name field
8. **Monitor time budget** in colored bar above table
9. **Export data** using CSV or JSON download buttons

## 📋 Data Fields

### Station Information
- **Station Name**: Marine organism name (editable) + Station Code (AB, XY, QR)
- **Latitude**: Decimal degrees (6 decimal places)
- **Longitude**: Decimal degrees (6 decimal places)
- **Distance**: Cumulative distance in nautical miles
- **Speed**: Ship speed in knots
- **Arrival**: Date and time (YYYY-MM-DD HH:MM format)
- **Departure**: Date and time (YYYY-MM-DD HH:MM format)
- **Duration**: Time on station in hours
- **Comments**: Free text notes (separate row)

### Automatic Calculations
- **Distance**: Haversine formula between consecutive stations
- **Travel time**: Distance ÷ Speed
- **Arrival times**: Previous departure + travel time
- **Time budget**: Deadline - Final arrival time
- **Smart updates**: Manual entries preserved, only affected stations recalculated

## 📂 File Formats

### CSV Format (10 columns)
```csv
Station ID,Station Code,Latitude,Longitude,Distance (nm),Speed (knots),Arrival,Departure,Duration (hrs),Comments
Huge_Shark,AB,42.123456,-70.987654,0,8,2024-01-15 08:00,2024-01-15 10:00,2,Starting point
Fast_Whale,XY,42.456789,-70.654321,25.5,8,2024-01-15 13:12,2024-01-15 15:00,1.8,Deep water station
```

### GeoJSON Format
```json
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-70.987654, 42.123456]
    },
    "properties": {
      "name": "Huge_Shark",
      "stationCode": "AB",
      "distance": 0,
      "speed": "8",
      "arrive": "2024-01-15 08:00",
      "departure": "2024-01-15 10:00",
      "duration": "2",
      "comments": "Starting point",
      "depth": ""
    }
  }]
}
```

## 🎨 Marine Organism Names

### Naming Patterns
- **Pattern 1**: 4-letter adjective + 5-letter organism = "Huge_Shark"
- **Pattern 2**: 5-letter adjective + 4-letter organism = "Large_Tuna"

### Word Lists

**Adjectives (74 total)**:
- 4-letter: Huge, Tiny, Long, Tall, Wide, Vast, Blue, Gray, Pink, Teal, Soft, Hard, Dull, Waxy, Sick, Weak, Hale, Lame, Dead, Live, Wild, Tame, Calm, Meek, Bold, Aged, Fast, Slow, Spry, Rare, Lean
- 5-letter: Large, Small, Giant, Gross, Stout, Lanky, Black, White, Brown, Green, Fuzzy, Hairy, Scaly, Slimy, Shiny, Sleek, Silky, Downy, Bushy, Leafy, Spiny, Alive, Frail, Hardy, Plump, Gaunt, Timid, Brave, Fierce, Agile, Young, Adult, Prime, Quick, Swift, Fleet, Nippy, Barred, Noble, Feral, Stray, Local, Alien

**Organisms (75 total)**:
- 4-letter: Tuna, Bass, Carp, Crab, Clam, Seal, Orca, Pike, Rudd, Tope, Hake, Sole, Ling, Chub, Dory, Goby, Newt, Frog, Toad, Duck, Swan, Loon, Coot, Gull, Tern, Ibis, Skua, Worm, Slug, Mola, Opah, Scad, Cero, Dace, Mink
- 5-letter: Shark, Trout, Perch, Bream, Skate, Smelt, Tench, Roach, Guppy, Molly, Tetra, Betta, Cisco, Porgy, Wahoo, Manta, Loach, Krill, Prawn, Shrimp, Snail, Whelk, Conch, Squid, Whale, Otter, Heron, Egret, Grebe, Stork, Goose, Crane, Gecko, Skink, Viper, Leech, Polyp, Coral, Hydra, Algae

**Total Combinations**: 2,745 unique names

## 🔧 Technical Details

### Technologies
- **Pure HTML/CSS/JavaScript** - no build process required
- **Leaflet.js** for interactive mapping
- **Tabulator** for advanced table features
- **Flatpickr** for datetime picking
- **LocalStorage** for data persistence

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Data Storage
- All data stored in browser's **localStorage**
- Survives browser restarts
- Per-domain storage (not cross-domain)
- No server required
- No external database needed

### Performance
- Handles **100+ stations** smoothly
- Pagination for large datasets (20 rows default)
- Efficient marker rendering
- Optimized table updates with `updateCellValues()`
- Preserved scroll positions
- No unnecessary re-renders

## 📖 Version History

### v2.2 (Current) - Manual Time Management
- **Bold green text** for manually set arrival/departure times
- **Unselect button (✕)** next to manually set times for quick revert
- Click unselect button to clear manual setting and recalculate downstream times
- Improved visual distinction between manual and calculated times
- Complete history tracking for manual time changes

### v2.1 - UI Polish & Fixes
- ID/# toggle switch for marker display
- Borderless table columns
- Compact pagination footer (white text)
- Time Budget bar repositioned above table (30% width, right-aligned)
- Perfect button alignment with invisible spacers
- Fixed datetime picker functionality (calendar + manual entry)
- Station column width increased to 130px
- Default page size: 20 rows
- Removed debug logging
- Marine organism station naming system
- Modern pill-style buttons with split pills
- Flatpickr datetime pickers
- Dark blue nautical theme
- Numbered marker badges
- Unique station codes (AB, XY, QR)
- Pagination support
- GeoJSON upload capability
- Station codes in export/import
- Royal blue editable fields

### v1.1.1 - Bug Fixes
- Custom station names preserved
- Map popups update correctly
- Speed apply confirmation dialog

### v1.1 - Time Budget
- Cruise start/end date tracking
- Real-time budget calculations
- Visual indicators (green/red)

### v1.0 - Initial Release
- Interactive map with draggable markers
- Two-row table layout
- CSV/GeoJSON export
- Undo functionality
- Resizable panels
- Setup modal

## 🎯 Use Cases

### Research Cruises
- Plan multi-day oceanographic surveys
- Track time constraints and deadlines
- Export data for ship crew
- Share routes with research team
- Toggle between numbered and ID markers

### Teaching
- Demonstrate marine route planning
- Calculate travel times and distances
- Visualize cruise logistics
- Export data for student analysis

### Expedition Planning
- Design sampling transects
- Optimize station placement
- Calculate fuel requirements
- Coordinate with other vessels
- Quick reference via station codes

## 🤝 Contributing

This is a standalone application. To modify:

1. Edit `route_planner.html` directly
2. Test in browser
3. Submit improvements via pull request

## 📄 License

MIT License - Free to use, modify, and distribute

## 🆘 Support

For issues or questions:
1. Check the **Setup Modal** help text
2. Review **CHANGELOG.md** for recent changes
3. Examine **PROJECT.md** for technical details
4. Open an issue on the repository

## 🙏 Acknowledgments

- **Leaflet** for mapping library
- **Tabulator** for table functionality
- **Flatpickr** for datetime picking
- **OpenStreetMap** for base map tiles
- Oceanographic community for feedback and testing

---

**Version 2.2** | Built for oceanographic research | No installation required | Works offline after first load

# weather_app-
draw a shape you want on a map and get the weather description 

##  Overview
This application demonstrates a complete GIS (Geographic Information System) workflow:
- **Frontend**: Users draw polygons on a Leaflet map
- **Backend**: Django processes and stores the geometries
- **Database**: PostGIS saves the spatial data
- **Integration**: Optional weather data from OpenWeatherMap API
##  Technologies Used
- **Django** : Python web framework 
- **GeoDjango** : Django's geographic extension 
- **PostGIS** : Spatial database (stores polygons) 
- **Leaflet.js** : Interactive maps in browser 
- **OpenWeatherMap API** : Weather data 
- **Bootstrap/CSS** : Styling and layout 
 ##  How It Works
- 1 Draw polygon
- 2 Send coordinates
- 3 Save to DB
- 4 Query weather
- 5 Display results
 ##  Prerequisites
Before you begin, ensure you have installed:
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **PostgreSQL 12+** - [Download](https://www.postgresql.org/download/)
- **PostGIS extension** - [Guide](https://postgis.net/install/)
- **Git** (optional) - [Download](https://git-scm.com/downloads)
## Usage Guide
**Drawing a Polygon**

Click on the map to add points (vertices)

Each click adds a numbered marker

Double-click to complete the polygon

The polygon turns green when complete

**Saving Data**

Click "Save Area to PostGIS"

**The app automatically:**

- Saves coordinates to database

- Fetches weather for the area

- Displays weather info

- Adds to saved list

**Viewing Saved Polygons**

All saved areas appear in the sidebar

Click any saved area to:

- Zoom to it on map

- View its weather data

- See when it was created

**Managing Drawings**

"Clear Drawing" - Remove current drawing

"Refresh List" - Update saved polygons list

## Quick Start 

**1. Clone and enter**

git clone https://github.com/calcuoumabac/weather_app-.git 

**2. Setup virtual environment**

python -m venv venv

venv\Scripts\activate  # Windows

**3. Install dependencies**

pip install -r requirements.txt

**4. Create database**

createdb gis_db

psql -d gis_db -c "CREATE EXTENSION postgis;"

**5. Run migrations**

python manage.py migrate

**6. Start server**

python manage.py runserver
 
 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import GEOSGeometry, Polygon
from .models import DrawnPolygon
import json
import requests


WEATHER_API_KEY = "f888b73f7838c63fababf119a2844966"  

def map_view(request):
    """Render the map page"""
    return render(request, 'map.html')

@csrf_exempt
def save_polygon(request):
    """Save polygon to database and get weather data"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Convert coordinates to Polygon
            coordinates = data['coordinates']
            
            # Ensure polygon is closed (first point = last point)
            if coordinates[0] != coordinates[-1]:
                coordinates.append(coordinates[0])
            
            # Create polygon
            geom = Polygon(coordinates)
            
            # Get centroid for weather
            centroid = geom.centroid
            
            # Fetch weather data
            weather = get_weather(centroid.y, centroid.x)
            
            # Save to database
            polygon = DrawnPolygon.objects.create(
                name=data.get('name', f'Polygon {DrawnPolygon.objects.count() + 1}'),
                geometry=geom,
                weather_data=weather
            )
            
            return JsonResponse({
                'success': True,
                'id': polygon.id,
                'weather': weather,
                'message': 'Polygon saved with weather data!'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_weather(lat, lon):
    """Fetch weather data from OpenWeatherMap"""
    if WEATHER_API_KEY == "f888b73f7838c63fababf119a2844966":
        return {
            'temperature': 22.5,
            'feels_like': 21.8,
            'humidity': 65,
            'description': 'clear sky',
            'wind_speed': 3.6,
            'city': 'Sample City'
        }
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        return {
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'city': data.get('name', 'Unknown')
        }
    except:
        return {
            'temperature': 'N/A',
            'description': 'Weather data unavailable',
            'error': 'Could not fetch weather'
        }

def get_polygons(request):
    """Get all saved polygons"""
    polygons = DrawnPolygon.objects.all().order_by('-created_at')
    features = []
    
    for poly in polygons:
        features.append({
            'id': poly.id,
            'name': poly.name,
            'geometry': json.loads(poly.geometry.geojson) if poly.geometry else None,
            'weather': poly.weather_data,
            'created_at': poly.created_at.strftime('%Y-%m-%d %H:%M')
        })
    
    return JsonResponse({'polygons': features})
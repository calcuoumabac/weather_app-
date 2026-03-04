from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('save-polygon/', views.save_polygon, name='save_polygon'),
    path('get-polygons/', views.get_polygons, name='get_polygons'),
]
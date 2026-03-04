from django.contrib.gis.db import models

class DrawnPolygon(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.PolygonField(srid=4326, null=True, blank=True)
    weather_data = models.JSONField(null=True, blank=True)  # Store weather info
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"
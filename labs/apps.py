# labs/apps.py
from django.apps import AppConfig

class LabsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labs'
    
    def ready(self):
        # Importe signals aqui se estiver usando
        pass
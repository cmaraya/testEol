from django.urls import path
from .views import read_json_file

urlpatterns = [
    path('read_data/', read_json_file, name='read_json'),
]

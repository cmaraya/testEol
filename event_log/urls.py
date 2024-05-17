from django.urls import path
from . import views

urlpatterns = [
    path('get_filter_event_logs/', views.get_filter_event_logs, name='get_filter_event_logs'),
    path('get_unique_usernames/', views.get_unique_usernames, name='get_unique_usernames'),
    path('get_unique_event_types/', views.get_unique_event_types, name='get_unique_event_types'),
    path('get_unique_event_sources/', views.get_unique_event_sources, name='get_unique_event_sources'),
    path('get_all_event_logs/', views.all_event_logs, name='all_event_logs'),

]

from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.shortcuts import render
from event_log.models import EventLog
from datetime import datetime, time 
from django.db.models import Q


def all_event_logs():
  event_logs = EventLog.objects.all()
  return event_logs

def get_unique_parameters(parameter):
  unique_parameters = EventLog.objects.values_list(parameter, flat=True).distinct()
  return unique_parameters

def get_unique_usernames():
  return get_unique_parameters('username')

def get_unique_event_types():
  return get_unique_parameters('event_type')

def get_unique_event_sources():
  return get_unique_parameters('event_source')

def get_evet_log_filters(request):
  start_hour = 17  # request.GET.get('start_hour')
  start_minute = 5  # request.GET.get('start_minute')
  end_hour = 18  # request.GET.get('end_hour')
  end_minute = 10  

  filters = {}
  if request.usernames:
      filters['username__in'] = request.usernames
  if request.event_type:
      filters['event_type'] = request.event_type
    # Aplicar los filtros
  if start_hour is not None and start_minute is not None and end_hour is not None and end_minute is not None:
    time_range_filter = (
        Q(timestamp__hour=start_hour, timestamp__minute__gte=start_minute) |
        Q(timestamp__hour__gt=start_hour, timestamp__hour__lt=end_hour) |
        Q(timestamp__hour=end_hour, timestamp__minute__lte=end_minute)
    )
    filtered_logs = filtered_logs.filter(time_range_filter)
  return filtered_logs[:request.cantidad]
# Create your views here.
from django.http import JsonResponse
from event_log.models import EventLog
from datetime import datetime
from django.utils.timezone import make_aware


def all_event_logs(request):
  item_to_show = request.GET.get('item_to_show')
  event_logs = EventLog.objects.all().values()[:int(item_to_show)]
  return JsonResponse(list(event_logs), safe=False)

def get_unique_parameters(parameter,tiems):
    # Obtener todos los logs de eventos
    event_logs = EventLog.objects.values(parameter)
    # Filtrar para incluir solo eventos del 03-04-2023
    start_date = datetime.strptime('2023-04-03', '%Y-%m-%d')
    end_date = start_date.replace(hour=23, minute=59, second=59)
    event_logs = event_logs.filter(time__range=(start_date, end_date))

    usernames = event_logs[:int(tiems)]
    usernames_list = list(usernames)
    return JsonResponse(usernames_list, safe=False)

def get_unique_usernames(request):
  item_to_show = request.GET.get('item_to_show')
  return get_unique_parameters('username',item_to_show)

def get_unique_event_types(request):
  item_to_show = request.GET.get('item_to_show')
  return get_unique_parameters('event_type',item_to_show)

def get_unique_event_sources(request):
  item_to_show = request.GET.get('item_to_show')
  return get_unique_parameters('event_source',item_to_show)

def get_filter_event_logs(request):
    # Obtener los parámetros de la solicitud
    item_to_show = request.GET.get('item_to_show')
    time = request.GET.getlist('time[]')  
    event_source = request.GET.get('source')
    usernames = request.GET.getlist('username[]') 
    event_type = request.GET.get('type')

    # Obtener todos los logs de eventos
    event_logs = EventLog.objects.all().values()

    # Filtrar para incluir solo eventos del 03-04-2023
    start_date = datetime.strptime('2023-04-03', '%Y-%m-%d')
    end_date = start_date.replace(hour=23, minute=59, second=59)
    event_logs = event_logs.filter(time__range=(start_date, end_date))

    # Filtrar por parámetros

    if time:
      # Transformar en fecha los datos de tiempo 
      inital_time = datetime.strptime(time[0], '%Y-%m-%d %H:%M:%S')
      end_time = datetime.strptime(time[1], '%Y-%m-%d %H:%M:%S')
      # reemplazar por el día 03-04-2023
      inital_time = inital_time.replace(year=2023,month=4,day=3)
      end_time = end_time.replace(year=2023,month=4,day=3)
      event_logs = event_logs.filter(time__range=(inital_time, end_time))

    if event_source:
        event_logs = event_logs.filter(event_source=event_source)
    
    if usernames:
        event_logs = event_logs.filter(username__in=usernames)
    
    if event_type:
        event_logs = event_logs.filter(event_type=event_type)

    
    # Obtener litas de parametros para los select
    unique_usernames = event_logs.values('username')[:int(item_to_show)]
    unique_event_types = event_logs.values('event_type')[:int(item_to_show)]
    unique_event_sources = event_logs.values('event_source')[:int(item_to_show)]

    # Obtener la cantidad pedida de eventos
    event_logs = event_logs[:int(item_to_show)]
    response_data = {
        'event_logs': list(event_logs),
        'event_types': list(unique_event_types),
        'event_sources': list(unique_event_sources),
        'usernames': list(unique_usernames),
    }
    # Devolver json con eventos y nuevos parametros de los select correcpondientes
    return JsonResponse(response_data, safe=False)

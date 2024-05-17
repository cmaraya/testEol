from django.contrib import admin
from .models import EventLog

# Register your models here.
@admin.register(EventLog)
class PlatoAdmin(admin.ModelAdmin):
  pass
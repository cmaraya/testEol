from django.db import models

# Create your models here.

class EventLog(models.Model):
    context = models.JSONField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True, default="")
    session = models.CharField(max_length=255, null=True, blank=True, default="")
    agent = models.CharField(max_length=255, null=True, blank=True, default="")
    host = models.CharField(max_length=255, null=True, blank=True, default="")
    referer  = models.CharField(max_length=255, null=True, blank=True, default="")
    accept_language = models.CharField(max_length=255, null=True, blank=True, default="")
    event = models.JSONField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    event_type = models.CharField(max_length=255, null=True, blank=True, default="")
    event_source = models.CharField(max_length=255, null=True, blank=True, default="")
    page = models.CharField(max_length=255, null=True, blank=True, default="")
    
from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True, default="")
    user_id = models.IntegerField(null=True, blank=True)

class Host(models.Model):
    host_name = models.CharField(max_length=255, null=True, blank=True, default="")

class AcceptLanguage(models.Model):
    language_name = models.CharField(max_length=255, null=True, blank=True, default="")

class EventSource(models.Model):
    source_name = models.CharField(max_length=255, null=True, blank=True, default="")

class EventType(models.Model):
    type_name = models.CharField(max_length=255, null=True, blank=True, default="")


class EventLog(models.Model):
    ## foreing keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    accept_language = models.ForeignKey(AcceptLanguage, on_delete=models.CASCADE)
    event_source = models.ForeignKey(EventSource, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    # atributes
    path = models.CharField(max_length=255, null=True, blank=True, default="")
    page = models.CharField(max_length=255, null=True, blank=True, default="")
    course_id = models.CharField(max_length=255, null=True, blank=True, default="")
    org_id = models.CharField(max_length=255, null=True, blank=True, default="")
    get_data = models.JSONField(null=True, blank=True)
    has_get = models.BooleanField(null=True, blank=True)
    post_data = models.JSONField(null=True, blank=True)
    has_post = models.BooleanField(null=True, blank=True)
    session = models.CharField(max_length=255, null=True, blank=True, default="")
    agent = models.CharField(max_length=255, null=True, blank=True, default="")
    referer  = models.CharField(max_length=255, null=True, blank=True, default="")
    time = models.DateTimeField(null=True, blank=True)

 
# Generated by Django 5.0.6 on 2024-05-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.JSONField(blank=True, null=True)),
                ('username', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('session', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('agent', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('host', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('referer', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('accept_language', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('event', models.JSONField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('event_source', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('page', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]

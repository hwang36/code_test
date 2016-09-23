import os
from django.db import models

class View_data(models.Model):
        device_id = models.CharField(max_length=10, null=True, blank=True)
        excel_data = models.DateField(null=True, blank=True)
        kwh = models.CharField(max_length=100, null=True, blank=True)
        power = models.CharField(max_length=100, null=True, blank=True)


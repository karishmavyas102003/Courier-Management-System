from django.contrib import admin
from .models import Courier, TrackingHistory

admin.site.register(Courier)
admin.site.register(TrackingHistory)
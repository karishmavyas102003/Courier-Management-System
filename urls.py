# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Django admin URLs
    # path('myapp/', include('myapp.urls')), # Includes URLs from the 'myapp' app
    path('', include('transworld.urls')), # Directs root path to 'blog' app's URLs
]

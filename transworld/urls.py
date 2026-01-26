"""
URL configuration for transworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views   # app name = main (photo pramane)




urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login/', views.home_view, name='login'),
    path('register/', views.registerForm, name='register'),
    path('AboutUs/', views.Aboutus, name='Aboutus'),
    path('track/', views.track_courier, name='track'),
    path('register/', views.register, name='register'),
    path('payment/', views.select_payment, name='payment'),
    
    
]
    




urlpatterns += static(settings.STATIC_URL)






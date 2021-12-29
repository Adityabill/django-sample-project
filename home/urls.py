from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('variable_profile', views.variableProfile, name='variable_profile'),
    path('services/software_development', views.service_soft_dev, name='software_development'),
    path('services/machine_learning', views.service_ml, name='machine_learning'),
    path('services/cloud_services', views.service_cloud_serv, name='cloud_services'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('api/sensor-data', views.value, name='api-route'),
    path('api/sensor-data/<int:id>', views.insert, name='update'),
    path('getData', views.getData, name='getData')
]
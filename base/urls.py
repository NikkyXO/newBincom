from django.urls import path
from base import views


urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.polling_units, name='units'),
    path('units/<int:id>/', views.pu_result, name='unit-result'),
    path('lgas/', views.lgas, name='lgas'),
    path('lgas/<int:id>/', views.lga_result, name='lga-result')
]
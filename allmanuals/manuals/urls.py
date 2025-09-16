from django.urls import path

from . import views

app_name = 'manuals'

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('<int:factory_id>/', views.bike_detail, name='bike_detail'),
]

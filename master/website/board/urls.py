from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
]

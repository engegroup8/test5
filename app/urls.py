from django.urls import path
from . import views

urlpatterns = [
    path('', views.instrument_function, name='instrument_function'),
]

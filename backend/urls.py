from django.urls import path
from .views import registration, deleteApp

urlpatterns = [
    path('delete/', deleteApp),
    path('', registration),
]
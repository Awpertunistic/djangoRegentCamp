from django.urls import path
from .views import registration, deleteApp, send_emails

urlpatterns = [
    path('delete/', deleteApp),
    path('emails/', send_emails),
    #path('update_reg_status/, '),
    path('send_emails', send_emails),
    path('register/', registration),
]

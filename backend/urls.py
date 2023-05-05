from django.urls import path
from .views import registration, delete_students, send_emails, update_status

urlpatterns = [
    path('delete/', delete_students),
    path('emails/', send_emails),
    path('update_reg_status/', update_status),
    path('send-emails/', send_emails),
    path('register/', registration),
]

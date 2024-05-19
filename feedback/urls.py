from django.urls import path
from .views import send_email


urlpatterns = [
    path('post/', send_email),
]

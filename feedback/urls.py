from django.urls import path
from .views import send_email, ContactList


urlpatterns = [
    path('post/', send_email),
    path('contact/', ContactList.as_view({'get': 'list'}), name='contact'),

]

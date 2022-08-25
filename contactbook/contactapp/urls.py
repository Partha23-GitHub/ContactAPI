from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from contactapp import views
urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('registration/',views.registration_view,name='registration'),
]
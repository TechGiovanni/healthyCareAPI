from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.hello_world),
    # send a post request with a username and password to create the token returns a token
    path('api-token-auth/', obtain_auth_token),
]

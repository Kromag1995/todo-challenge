from django.urls import path
from .views import signin_view, login_view, logout_view

urlpatterns = [
    path('signin/', signin_view),
    path('login/',login_view),
    path('logout/',logout_view),
]
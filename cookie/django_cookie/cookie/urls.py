from django.urls import path
from .views import * 

urlpatterns = [
    path('home/', home, name='home'),
    path('', login, name='login'),
    path('logout/', logout, name='logout')
]
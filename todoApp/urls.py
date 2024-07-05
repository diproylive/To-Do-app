
from django.urls import path
from .views import index , delete , log_in , log_out , register



urlpatterns = [
    path('', index , name ='index'),
    path('delete/<int:id>/', delete , name ='delete'),
    path('login/', log_in , name='log_in'),
    path('logout/', log_out , name='log_out'),
    path('register/', register , name='register'),
]
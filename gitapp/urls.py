from django.urls import path,include
from. import views

urlpatterns = [
    path('login',views.loginfn,name='login'),
]
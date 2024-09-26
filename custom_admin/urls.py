from django.urls import path , include
from custom_admin import views

app_name = 'custom_admin'

urlpatterns = [
    path('index/',views.test),
]
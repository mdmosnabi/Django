from django.urls import path
from userauths import views

urlpatterns = [
    path('sing-up/',views.register_view , name='sing-up'),
    path('sing-in/',views.login_view , name='sing-in'),
    path('sing-out/',views.logout_view , name='sing-out'),
]

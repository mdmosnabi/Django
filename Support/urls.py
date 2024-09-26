from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.ChatListView.as_view(), name='chat-list'),
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    
    path('', views.chat_list, name='chat_list'),
    path('create/', views.create_chat, name='create_chat'),
    path('chat/<str:cid>/', views.chat_room, name='chat_room'),
]

from rest_framework import generics, permissions
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required

class ChatListView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


##############      function view ###########

@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'support/chat_list.html', {'chats': chats})

@login_required
def chat_room(request, cid):
    chat = get_object_or_404(Chat, cid=cid)
    if request.user not in chat.participants.all():
        return redirect('chat_list')

    return render(request, 'support/chat_room.html', {'chat': chat})

@login_required
def create_chat(request):
    if request.method == 'POST':
        chat_name = request.POST['chat_name']
        chat = Chat.objects.create(chat_name=chat_name)
        chat.participants.add(request.user)
        return redirect('chat_room', cid=chat.cid)

    return render(request, 'support/create_chat.html')
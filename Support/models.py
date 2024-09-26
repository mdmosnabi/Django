from django.db import models
import shortuuid
from django.utils import timezone
from userauths.models import User

class Chat(models.Model):
    cid = models.CharField(unique=True, max_length=20)
    chat_name = models.CharField(max_length=255, default='default_room')
    participants = models.ManyToManyField(User, related_name='chats')
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.cid:
            self.cid = shortuuid.ShortUUID(alphabet='abcdefgh12345').random(length=10)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.chat_name
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(default='')
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username}: {self.content[:20]}'

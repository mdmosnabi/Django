from django.contrib import admin
from Support.models import Chat , Message

class ChatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Chat._meta.fields]
    
class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]

# Register your models here.
admin.site.register(Chat , ChatAdmin)
admin.site.register(Message,MessageAdmin)

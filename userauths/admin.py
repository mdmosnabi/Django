from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','bio','password']

admin.site.register(User,UserAdmin)

# Register your models here.

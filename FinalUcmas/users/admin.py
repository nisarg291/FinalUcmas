from django.contrib import admin
from .models import Profile,UserOTP,Notification

admin.site.register(Profile)
admin.site.register(UserOTP)
admin.site.register(Notification)
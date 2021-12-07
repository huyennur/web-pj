from django.contrib import admin
from .models import Message, PrivateRoom, MessageNotification
# Register your models here.
admin.site.register(Message)


class Message(admin.TabularInline):
    model = Message


class PrivateRoomAdmin(admin.ModelAdmin):
    inlines = [Message]

    class Meta:
        model = PrivateRoom


admin.site.register(PrivateRoom, PrivateRoomAdmin)
admin.site.register(MessageNotification)

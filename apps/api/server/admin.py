from django.contrib import admin

from .models import Event, Album, Media, Official, Official_Social, Official_Position

# Register your models here.

admin.site.register(Event)
admin.site.register(Album)
admin.site.register(Media)
admin.site.register(Official)
admin.site.register(Official_Social)
admin.site.register(Official_Position)

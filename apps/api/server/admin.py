from django.contrib import admin

from .models import Event, Album, Media, Official, Social

# Register your models here.

admin.site.register(Event)
admin.site.register(Album)
admin.site.register(Media)
admin.site.register(Official)
admin.site.register(Social)

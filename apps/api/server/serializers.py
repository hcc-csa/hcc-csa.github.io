from rest_framework import serializers
from .models import Event, Album, Media, Official, Official_Social, Subscribers

class MediaSerializer(serializers.ModelSerializer):

  class Meta:
    model = Media
    fields = ('__all__')

class AlbumSerializer(serializers.ModelSerializer):

  media = MediaSerializer(many=True)
  class Meta:
    model = Album
    fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):

  album = AlbumSerializer()

  class Meta:
    model = Event
    fields = ('__all__')

from rest_framework import serializers
from .models import Event, Album, Media, Officials, Social, Subscribers

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'

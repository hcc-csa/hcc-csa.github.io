from django.urls import path

from . import views

urlpatterns = [
    path('event/', views.EventListCreate.as_view(), name='event-create-view'),
    path('event/<int:pk>/', views.EventRetrieveUpdateDestroy.as_view(), name='event-update-view')
]

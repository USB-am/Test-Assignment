from django.urls import path

from .views import ParticipantsListView


urlpatterns = [
    path('', ParticipantsListView.as_view(), name='participants_list'),
]
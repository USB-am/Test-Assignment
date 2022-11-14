from django.shortcuts import render
from django.views.generic import ListView

from registration.models import Participant


class ParticipantsListView(ListView):
	''' Представление списка зарегестрированных участников '''
	model = Participant
	template_name = 'participants_list/participants_list.html'
	context_object_name = 'participants'
	paginate_by = 10
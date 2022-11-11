from django.shortcuts import render
from django.views.generic import ListView


class ParticipantsListView(ListView):
	''' Представление списка зарегестрированных участников '''
	template_name = 'participants_list/participants_list.html'
	# Определить модель 
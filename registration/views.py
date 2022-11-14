from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Participant
from .forms import RegistrationForm


class RegistrationView(CreateView):
	''' Представление формы регистрации '''
	template_name = 'registration/registration.html'
	model = Participant
	fields = '__all__'
	success_url = reverse_lazy('participants_list')

	def post(self, request, *args, **kwargs):
		form = RegistrationForm(request.POST)
		return super().post(request, *args, **kwargs)
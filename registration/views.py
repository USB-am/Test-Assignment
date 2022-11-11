from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import Participant
from .forms import RegistrationForm


class RegistrationView(CreateView):
	''' Представление формы регистрации '''
	template_name = 'registration/registration.html'
	model = Participant
	fields = '__all__'

	def post(self, request, *args, **kwargs):
		form = RegistrationForm(request.POST)

		#if form.is_valid():
		#	return redirect('home_page')
		print(f'Form is {form.is_valid()} valid!')

		return super().post(request, *args, **kwargs)
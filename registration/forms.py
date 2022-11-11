from django import forms

from .models import Participant


class RegistrationForm(forms.Form):
	class Meta:
		model = Participant
		fields = '__all__'
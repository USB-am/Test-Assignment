from django.db import models
from django.urls import reverse_lazy


class Participant(models.Model):
	''' Модель участка олимпиады '''
	name = models.CharField(max_length=100, verbose_name='Ф.И.О. участника')
	institution = models.CharField(max_length=255, verbose_name='Учебное заведение')
	phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
	email = models.EmailField(max_length=100, verbose_name='E-mail')

	class Meta:
		verbose_name = 'Участник'
		verbose_name_plural = 'Участники'
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse_lazy('home_page')
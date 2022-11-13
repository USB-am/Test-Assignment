from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	''' Представление главной страницы '''

	template_name = 'home_page/home_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['commitet'] = [i for i in range(8)]
		return context
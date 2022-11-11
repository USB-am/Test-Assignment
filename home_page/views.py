from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	''' Представление главной страницы '''

	template_name = 'home_page/home_page.html'
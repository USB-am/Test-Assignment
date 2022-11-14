from django.shortcuts import render
from django.views.generic import TemplateView


commitet_humans = [
	{
		'name': 'Darth Vader',
		'description': 'Darth Vader is a fictional character in the Star Wars franchise',
	},
	{
		'name': 'Yoda',
		'description': 'один из главных персонажей «Звёздных войн», Гранд-мастер Ордена джедаев, один из сильнейших и мудрейших джедаев своего времени',
	},
	{
		'name': 'Ahsoka Tano',
		'description': 'Впервые представленная в качестве джедая-падавана Энакина Скайуокера',
	},
	{
		'name': 'Darth Maul',
		'description': 'тёмный владыка ситхов, ученик Дарта Сидиуса',
	},
	{
		'name': 'Dooku',
		'description': 'Главный антагонист в фильме «Звёздные войны. Эпизод II: Атака клонов»',
	}
]


class HomePageView(TemplateView):
	''' Представление главной страницы '''

	template_name = 'home_page/home_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['commitet'] = enumerate(commitet_humans)
		context['gallery'] = [i for i in range(15)]
		return context
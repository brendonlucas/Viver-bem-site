from django.urls import path

from core.views import *

urlpatterns = [

    path('', home_page, name='home'),
    path('comida_e_saude', food_health_page, name='comida_saude'),
    path('bem_estar', well_being_page, name='bem_estar'),
    path('quiz/', quiz_page, name='quizzes'),
    path('quiz_frutas/', quiz_frutas, name='quiz_frutas'),
    path('about', about_page, name='sobre'),
]

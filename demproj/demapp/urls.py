from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name='home'),
    path("api/get_uizz/",views.get_uizz,name='get_uizz'),
    path("quiz/<int:nums>/",views.quiz,name='quiz'),
]

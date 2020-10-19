# Use include() to add paths from the tes_app application 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'), # Pagina principal
    path('palindroma/',views.words_page,name='words_page'), # Pagina secundaria
]
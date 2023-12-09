from django.urls import path
from fichas_api import views

urlpatterns = [
    path('ola-ficha', views.FichaView.as_view()),
]

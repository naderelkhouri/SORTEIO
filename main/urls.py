from django.urls import path
from . import views

urlpatterns = [
    path('sorteio/', views.sorteio, name="sorteio"),
]

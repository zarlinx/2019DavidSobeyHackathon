from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='payzant_index'),
    path('<str:itemnumber>/', views.prediction, name='prediction'),
]

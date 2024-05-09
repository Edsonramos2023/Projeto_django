from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('recepes/<int:id>/', views.recepe),
]

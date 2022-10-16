from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('pessoa/', views.pessoa),
    path('criar/', views.create_pessoa),
]
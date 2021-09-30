from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('howto/', views.HowTo, name='howto'),
    path('predict/', views.Predict, name='')
]
from django.urls import path

from . import views


urlpatterns = [
   path("dp/", views.deep_learning, name='deep'),
]
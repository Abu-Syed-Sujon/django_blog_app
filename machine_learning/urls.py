from django.urls import path

from . import views


urlpatterns = [
   path("machine/",views.machine_learning, name='ml'),
   path("dtr/",views.dtree, name='dt'),
   path("knn/",views.k_nearest, name='knn'),
   path("random/",views.random, name='random'),
] 
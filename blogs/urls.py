from django.urls import path

from . import views


urlpatterns = [
   path("blg/",views.blog1, name='blog'),
   path("frm/",views.showfromsdata),
]
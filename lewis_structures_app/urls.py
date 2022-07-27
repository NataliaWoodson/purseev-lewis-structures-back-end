from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/electrons/bond", views.bond, name="bond")
]

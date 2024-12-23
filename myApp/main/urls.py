from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("<int:id>", views.users, name="users"),
    #path("contact/", views.contact, name="contact"),
]
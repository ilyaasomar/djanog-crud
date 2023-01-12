from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.createCustomer, name="register"),
    path("update/<int:id>", views.selectData, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),


]
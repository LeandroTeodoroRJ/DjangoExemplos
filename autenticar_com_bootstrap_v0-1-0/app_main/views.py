from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):  #Render template for GET request
    template_name = "app_main/pages/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context["<template_var>"] = <value>    #Variáveis internas do html
        return context

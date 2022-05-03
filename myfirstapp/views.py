import imp
from re import template
from django.shortcuts import render
from django.views import generic


class home(generic.TemplateView):
    template_name='index.html'

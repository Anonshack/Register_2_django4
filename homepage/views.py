from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageBaseView(TemplateView):
    template_name = 'base.html'
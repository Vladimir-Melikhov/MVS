from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProjectsModel


class MainListView(ListView):
    model=ProjectsModel
    template_name="main/main_page.html"

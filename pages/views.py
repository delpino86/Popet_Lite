from django.shortcuts import render
from .models import  Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PagesDetailView(DetailView):

    model = Page

class PagesListView(ListView):

    model = Page
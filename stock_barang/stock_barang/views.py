from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView , RedirectView, View


def index (request):
     context = {
          'title' : 'manajement stock',

     }
     return render (request, 'index.html',context)

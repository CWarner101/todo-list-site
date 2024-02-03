# Name: Connor Warner
# Class: CIS 218
# Date: 2/7/24

from django.views.generic import ListView

from .models import Todo

class HomePageView(ListView):
    """Home Page View"""
    model = Todo
    template_name = 'home.html'
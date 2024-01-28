"""
Name: Connor Warner
Class: CIS 218
Date: 2/7/24
"""


from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home Page View"""
    template_name = "home.html"
# Name: Connor Warner
# Class: CIS 218
# Date: 2/7/24

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home')
]

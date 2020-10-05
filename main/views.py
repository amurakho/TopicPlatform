from django.shortcuts import render
from django.views.generic import ListView

from main.models import Link


class MainView(ListView):
    model = Link


class ScrappersRunView():
    pass


class ScrappingStatusView():
    pass
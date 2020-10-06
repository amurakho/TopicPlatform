from django.shortcuts import render
from django.views.generic import ListView

from main.models import Link


class MainView(ListView):
    model = Link
    queryset = {
        'with_keyword': Link.objects.filter(is_keyword=True)[:20],
        'without_keyword': Link.objects.filter(is_keyword=False)[:20],
    }
    template_name = 'links_lists.html'


class ScrappersRunView():
    pass


class ScrappingStatusView():
    pass
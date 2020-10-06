from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin

from main.models import Link
from main.forms import ScrapperLauncherForm


class MainView(FormMixin, ListView):
    model = Link
    queryset = {
        'with_keyword': Link.objects.filter(is_keyword=True)[:20],
        'without_keyword': Link.objects.filter(is_keyword=False)[:20],
    }
    template_name = 'links_lists.html'
    form_class = ScrapperLauncherForm

    def form_valid(self, form):
        keywords = form.cleaned_data['keywords'].split(',')
        # todo:

class ScrappingStatusView():
    pass
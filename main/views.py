from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin

from main.models import Link
from main.forms import ScrapperLauncherForm
from main.tasks import add


class MainView(FormMixin, ListView):
    model = Link
    queryset = {
        'with_keyword': Link.objects.filter(is_keyword=True)[:20],
        'without_keyword': Link.objects.filter(is_keyword=False)[:20],
    }
    template_name = 'links_lists.html'
    form_class = ScrapperLauncherForm

    def post(self, *args, **kwargs):
        if self.request.is_ajax:
            # todo: CELERY LAUNCH SCRAPPERS
            add.delay(2, 5)
            return JsonResponse({'status': 'OK'}, status=200)
        return JsonResponse({'error': ''}, status=400)


class ScrappingStatusView():
    pass
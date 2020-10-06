from django import forms
from django.conf import settings


class ScrapperLauncherForm(forms.Form):
    SCRAPPERS_CHOICE = ((scrapper, scrapper) for scrapper in settings.SCRAPPERS)

    all_scrappers = forms.BooleanField(widget=forms.CheckboxInput, initial=True)
    scrappers = forms.ChoiceField(choices=SCRAPPERS_CHOICE, disabled=True)
    keywords = forms.CharField(help_text='Write keywords separated by comma(",")')

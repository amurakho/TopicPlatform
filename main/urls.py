from django.urls import path

from main.views import MainView, launch_scrapper

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('lauch-scrapper/', launch_scrapper, name='launch')
    # path()
]
from django.urls import path

from api.views import LinksListView

urlpatterns = [
    path('links/', LinksListView.as_view())
]
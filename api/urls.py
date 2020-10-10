from django.urls import path

from api.views import LinksListView, LinkDetailView

urlpatterns = [
    path('links/', LinksListView.as_view()),
    path('links/<int:pk>/', LinkDetailView.as_view()),
]
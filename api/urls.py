from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import LinkViewSet

router = DefaultRouter()

router.register(r'links', LinkViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]

# from api.views import LinksListView, LinkDetailView
#
# urlpatterns = [
#     path('links/', LinksListView.as_view()),
#     path('links/<int:pk>/', LinkDetailView.as_view()),
# ]
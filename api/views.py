from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from main.models import Link
from api.serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )
    queryset = Link.objects.all()
    serializer_class = LinkSerializer



# class LinksListView(ListCreateAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.all()
#
#
# class LinkDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.all()


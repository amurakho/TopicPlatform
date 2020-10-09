from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Link
from api.serializers import LinkSerializer


class LinksListView(APIView):

    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)


class LinkDetailView(APIView):

    def get(self, request, pk):
        link = Link.objects.get(pk=pk)
        serializer = LinkSerializer(link)
        return Response(serializer.data)
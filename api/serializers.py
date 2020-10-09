from rest_framework.serializers import ModelSerializer

from main.models import Link


class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        # fields = ('url', 'title', 'pub_date', 'text', 'scrapped', 'is_keyword')
        fields = '__all__'

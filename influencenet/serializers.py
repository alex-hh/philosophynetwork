from rest_framework import serializers
from influencenet.models import InfluenceNode


class InfluenceNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluenceNode
        fields = ('freebase_id', 'name', 'date_of_birth')

from django.shortcuts import render
from django.http import JsonResponse
from .models import InfluenceEdge
# Create your views here.


def fulllist(request):
    edges = InfluenceEdge.objects.values_list('influencer__name', 'influencer__freebase_id', 'follower__name', 'follower__freebase_id')
    edge_dicts = [{'influencer_name': edge[0],
                   'influencer_id': edge[1],
                   'follower_name': edge[2],
                   'follower_id': edge[3]} for edge in edges]
    # edges = [{'follower_name':, 'follower_id', '}]
    return JsonResponse(edge_dicts, safe=False)

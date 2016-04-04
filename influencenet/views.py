from django.shortcuts import render
from django.http import JsonResponse
from .models import InfluenceEdge
# Create your views here.


def philosopher_edges(request):
    edges = InfluenceEdge.objects.filter(influencer__is_philosopher=True, follower__is_philosopher=True).values_list('influencer__name', 'influencer__freebase_id', 'follower__name', 'follower__freebase_id')
    edge_dicts = [{'influencer_name': edge[0],
                   'influencer_id': edge[1],
                   'follower_name': edge[2],
                   'follower_id': edge[3]} for edge in edges]
    # roughly 6000 edges here
    # edges = [{'follower_name':, 'follower_id', '}]
    return JsonResponse(edge_dicts, safe=False)


def landing(request):
    return render(request, 'influencenet/landing.html')

from django.shortcuts import render
from django.http import JsonResponse
from .models import InfluenceEdge

from django.views.generic import TemplateView

from django.db.models import Q
# Create your views here.


def philosopher_edges(request):
    edges = InfluenceEdge.objects.filter(influencer__is_philosopher=True, follower__is_philosopher=True).values_list('influencer__name', 'influencer__freebase_id', 'follower__name', 'follower__freebase_id')
    # i want my list of nodes to be like this:
    # [{'name': , 'id': , 'degree'}]
    edge_dicts = [{'influencer_name': edge[0],
                   'influencer_id': edge[1],
                   'follower_name': edge[2],
                   'follower_id': edge[3]} for edge in edges]
    # roughly 6000 edges here
    # edges = [{'follower_name':, 'follower_id', '}]
    return JsonResponse(edge_dicts, safe=False)


class LandingView(TemplateView):
    template_name = 'influencenet/landing.html'


class BuildNetworkView(TemplateView):
    template_name = 'influencenet/network_builder.html'


def d3_from_list(request):
    selected_nodes = ['/m/' + idstr for idstr in request.GET.getlist('pid')]
    edges = list(InfluenceEdge.objects.filter(Q(influencer__freebase_id__in=selected_nodes) |
                                         Q(follower__freebase_id__in=selected_nodes)).filter(
                                         influencer__is_philosopher=True,
                                         follower__is_philosopher=True).values_list(
                                         'influencer__name',
                                         'influencer__freebase_id',
                                         'follower__name',
                                         'follower__freebase_id'
                                         ))
    nodes = {(node, fbid) for edge in edges
             for node, fbid in ((edge[0], edge[1]),(edge[2], edge[3]))}
    node_ids = [fbid for name, fbid in nodes if fbid not in selected_nodes]
    edges += list(InfluenceEdge.objects.filter(influencer__freebase_id__in=node_ids,
                                          follower__freebase_id__in=node_ids).values_list(
                                         'influencer__name',
                                         'influencer__freebase_id',
                                         'follower__name',
                                         'follower__freebase_id'
                                         ))
    nodes = {(node, fbid) for edge in edges
             for node, fbid in ((edge[0], edge[1]),(edge[2], edge[3]))}
    nodes = [{'name': name, 'id': fbid} for name, fbid in nodes]
    node_lookup = list(map(lambda x: x['id'], nodes))
    print(node_lookup)
    edges = [{'source': node_lookup.index(edge[1]), 'target': node_lookup.index(edge[3])}
             for edge in edges]
    payload = {'nodes': nodes, 'edges': edges}
    return JsonResponse(payload, safe=False)

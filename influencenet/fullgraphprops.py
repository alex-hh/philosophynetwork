# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 02:24:08 2015

@author: alexhooker
"""

import pandas as pd
import networkx as nx
import numpy
import matplotlib.pyplot as plt
import pygraphviz
import math

edges = pd.read_csv('fulllist.csv', encoding = 'utf-8')

#edges[(edges.name_x == 'Zadie Smith') | (edges.name_y == 'Zadie Smith')]
H = nx.DiGraph()
#phil = edges[(edges.phil_x == 1) & (edges.phil_y == 1)]
#phil = phil.dropna(subset = ['name_x', 'name_y'])
#H.add_edges_from(numpy.array(phil[['name_x', 'name_y']]))
edges = edges.dropna(subset = ['name_x', 'name_y'])
H.add_edges_from(numpy.array(edges[['name_x', 'name_y']]))

d = nx.degree(H)
k = nx.katz_centrality_numpy(H.reverse(), alpha = 0.075, beta = 1)
#b = nx.betweenness_centrality(H)
s = pd.Series(k, name = 'kc_score')
s.index.name = 'name'
s.reset_index()
s.sort('kc_score', ascending=False)
print (s[0:60])


#nx.ancestors(H, 'Plato')
#plt.figure(figsize = (50,50))
#try:
#pos=nx.graphviz_layout(H, prog='dot')
#except:
#        pos=nx.spring_layout(H,iterations=20)
#pos = nx.spring_layout(H,iterations=20)
#labels = nx.nodes(H)
#nx.draw_networkx_nodes(H, pos, node_size = nodesizes)
#nx.draw_networkx_edges(H, pos, weight = 0.1, arrows = False, alpha = 0.5, style = 'dashed')
#nx.draw_networkx_labels(H, pos, font_size = 30)
#nx.draw(H, pos, arrows=False)

#plt.savefig(outfile)

# k is optimal distance between nodes. Optimal distance between nodes. If None the distance is set to 1/sqrt(n) where n is the number of nodes. Increase this value to move nodes farther apart.
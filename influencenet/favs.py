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

favourites = []
i=0
while i < 9:
  w1 = str(input("Name a favourite writer: "))
  favourites.append(w1)
  i = i+1

outfile = str(input("Graph file name e.g. 'graph.png'"))


#favourites = ['John Banville','Bret Easton Ellis','Samuel Beckett','Franz Kafka','Milan Kundera','Arthur Koestler','Michel Houellebcq', 'Jorge Luis Borges','David Mitchell','Jack Kerouac']

degrees = []
nodesizes = []

#edges['name_x'].str.encode('utf-8')
#edges['name_y'].str.encode('utf-8')

H = nx.DiGraph()

#does my network generator depend on order? no
def new_net(favourites):
  H.clear()
  for i in favourites:
    for j in numpy.array(edges[edges['name_x'] == i]['name_y']):
        H.add_edge(i,j)
    for j in numpy.array(edges[edges['name_y']== i]['name_x']): #should these perhaps have less weight
        H.add_edge(j,i)
  for i in nx.nodes(H):
      for j in numpy.array(edges[edges['name_x'] == i]['name_y']):
          if H.degree(j) != {}:
              H.add_edge(i,j)  
  for n in nx.nodes(H) :
      degrees.append([n, H.degree(n), H.out_degree(n)])
      if (H.out_degree(n) < 10) and (n not in favourites):
         H.remove_node(n)
      else:
        nodesizes.append(150*H.degree(n))

#  i=0
#  while i < len(degrees):
#    degs = degrees[i]
#    phil = degs[0]
#    secdeg = 0
#    for j in H.edges(phil):
#        secdeg = secdeg + H.out_degree(j[1])
    
    #    degs.append(secdeg)
#    i = i+1
        
#  od = pd.DataFrame(degrees, columns=['name', 'deg', 'out_deg', '2nddegout'])
  od = pd.DataFrame(degrees, columns=['name', 'deg', 'out_deg'])
#  score = od['out_deg'] + (0.5* od['2nddegout'])
#  od.loc[:,'score'] = score


  return od

od = new_net(favourites)

for i in H.nodes():
    try:
        if math.isnan(i):
            H.remove_node(i)
    except:
        pass

#nx.katz_centrality(H) this finds in edges. for out edges first reverse the graph with H.reverse()
    
#q = """
#    SELECT *
#    FROM od
#    ORDER BY deg DESC
#    """
    
#query = pandasql.sqldf(q.lower(), locals())



d = nx.degree(H)
plt.figure(figsize = (50,50))
#try:
pos=nx.graphviz_layout(H, prog='dot')
#except:
#        pos=nx.spring_layout(H,iterations=20)
#pos = nx.spring_layout(H,iterations=20)
#labels = nx.nodes(H)
nx.draw_networkx_nodes(H, pos, node_size = nodesizes)
nx.draw_networkx_edges(H, pos, weight = 0.1, arrows = False, alpha = 0.5, style = 'dashed')
nx.draw_networkx_labels(H, pos, font_size = 30)
#nx.draw(H, pos, arrows=False)

plt.savefig(outfile)

# k is optimal distance between nodes. Optimal distance between nodes. If None the distance is set to 1/sqrt(n) where n is the number of nodes. Increase this value to move nodes farther apart.
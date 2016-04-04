# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:24:17 2015

@author: alexhooker
"""

import json
import pandas as pd
import networkx as nx
import pprint
import numpy

f = open('newdata.txt')
fb = json.load(f)


#every index in fb['result'] is a dictionary whose keys are count, name, influenced, mid.

g = open('jsonfb.txt')
gb = json.load(g)

idopen = open('ids.txt')
ids = json.load(idopen)
iddf = pd.DataFrame(ids['result'])
iddf.pop('type')

philidopen = open('philids.txt')
philids = json.load(philidopen)
philiddf = pd.DataFrame(philids['result'])

philiddf['phil'] = pd.Series(numpy.ones(len(philiddf)))
philiddf = philiddf.drop(['type','profession'],1)

iddff = pd.merge(iddf, philiddf, on=['mid','name'], how='outer')

writidopen = open('writids.txt')
writids = json.load(writidopen)
writiddf = pd.DataFrame(writids['result'])

writiddf['writ'] = pd.Series(numpy.ones(len(writiddf)))
writiddf = writiddf.drop(['type','profession'],1)

iddff = pd.merge(iddff, writiddf, on = ['mid','name'], how='outer')

dbpedges1 = pd.read_csv('dbpedgelist.csv')
dbpedges2 = pd.read_csv('sparql (3).csv')
dbpedges3 = pd.read_csv('sparql (4).csv')

edges = pd.concat([dbpedges1, dbpedges2, dbpedges3])
trimmed = edges.replace({'http://rdf.freebase.com/ns': ''}, regex=True)
edgestrimmed = trimmed.replace({'m.0': 'm/0'}, regex=True)
edgestrimmed['fb1'][edgestrimmed.fb1 == '/m/0m/0c'] = '/m/0mj0c' #corrects william james' key

influencelist = fb['result']

h=[]
for i in influencelist:
     entry = i
     influences = entry['influenced']
     key = entry['mid']
     df = edgestrimmed[edgestrimmed['fb1'] == key]
     for j in influences:
        id = j['mid']
        if ((df['fb2']==id).any() == False):
            h.append([key, id])

p = pd.DataFrame(h, columns = ['fb1', 'fb2'])
edgestrimmed = pd.concat([edgestrimmed, p])
edgestrimmed['fb1'][edgestrimmed.fb1 == '/m/0m/0c'] = '/m/0mj0c'

k = pd.merge(edgestrimmed, iddff, left_on='fb1', right_on='mid', how='left')
k.pop('mid')
k = pd.merge(k, iddff, left_on='fb2',right_on='mid', how='left')
k.pop('mid')

print(k[k['fb1'] == '/m/0350t'])


phil = k[(k['phil_x'] ==1) | (k['phil_y'] == 1)]
phil.loc[:,'name_xmiss'] = pd.isnull(phil['name_x'])

#k.to_csv('new.csv', encoding = 'utf-8')

#/m/0m/0c should be /m/0mj0c
#phil.dropna(axis=0)

#print (influencelist)

#print(influencelist[1])
#y = (influencelist[1]['influenced'][1]['mid'])
#df = (k[k['fb1']== y])
#print (df)
#print('/m/042q3' in df['fb2'])
#print((df['fb2'] == '/m/042q3').any())
#print((df['fb2'] == '/m/042q45').any() == False)

#h = pd.DataFrame(columns=['fb1','fb2','name_x','name_y'])

#h = []

#for i in influencelist:
#     entry = i
#     influences = entry['influenced']
#     key = entry['mid']
#     phil_x = iddff[iddff['mid'] == key]['phil']
#     name_x = entry['name']
#     writ_x = iddff[iddff['mid'] == key]['writ']
#     df = k[k['fb1'] == key]
#     for j in influences:
#        id = j['mid']
#        name_y = j['name']
#        phil_y = iddff[iddff['mid'] == key]['phil']
#        writ_y = iddff[iddff['mid'] == key]['writ']
#        if ((df['fb2']==id).any() == False):
#            h.append([key, id, name_x, phil_x, writ_x, name_y, phil_y, writ_y])


#p = pd.DataFrame(h, columns = ['fb1', 'fb2', name_x, phil_x, writ_x, name_y, phil_y, writ_y])
#p.to_csv('freebaseinfo.csv')

#print(p)

#fulllist = pd.concat([k, p])
#print(fulllist[fulllist['fb1'] == '/m/0350t'])

#    pdict.pop('count', None)
#    pdict.pop('type', None)
#    influencerid = list(pdict['mid'])
#    influencerid[2] = '.'
    
#    dbpedges = edges[edges]
    
    
    


# test case: '/m/0350t' is Fichte who is fb['result'][1]
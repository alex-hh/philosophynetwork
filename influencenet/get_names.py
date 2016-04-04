import csv
import re
from influencenet.models import Philosopher,InfluenceNode,InfluenceEdge

def add_philosophers_to_db():
	with open('philnet/static/fulllist.csv', newline='',encoding='utf-8') as csvfile:
		reader=csv.DictReader(csvfile,delimiter=',')
	#If the fieldnames parameter is omitted, the values in the first row of the csvfile will be used as the fieldnames
	#'fb1', 'fb2', 'name_x', 'phil_x', 'writ_x', 'name_y','phil_y', 'writ_y'
		for row in reader:
			if row['name_x'] and row['phil_x']=='1.0':
				phil = InfluenceNode.objects.filter(name=row['name_x']).first()
				phil.is_philosopher=True
				phil.save()
				print(phil.name,phil.is_philosopher)
			if row['name_y'] and row['phil_y']=='1.0':
				phil = InfluenceNode.objects.filter(name=row['name_y']).first()
				phil.is_philosopher=True
				phil.save()
			# if row['name_x'] and not InfluenceNode.objects.filter(name=row['name_x']).all():
			# 	new_phil = InfluenceNode(name=row['name_x'],freebase_id=row['fb1'])
			# 	new_phil.save()
			# if row['name_y'] and not InfluenceNode.objects.filter(name=row['name_y']).all():
			# 	new_node=InfluenceNode(name=row['name_y'],freebase_id=row['fb2'])
			# 	new_node.save()

def add_phil_from_db():
	with open('influencenet/dbpphilids.csv',newline='',encoding='utf-8') as csvfile:
		reader=csv.DictReader(csvfile,delimiter=',')
		for row in reader:
			fb = re.sub("http://rdf.freebase.com/ns","",row['influenced'])
			fb_id = re.sub("/m.","/m/",fb)
			phil = InfluenceNode.objects.filter(freebase_id=fb_id).first()
			if phil and not phil.is_philosopher:
				phil.is_philosopher=True
				phil.save()
				print(phil.name)

def add_edges():
	with open('philnet/static/fulllist.csv', newline='',encoding='utf-8') as csvfile:
		reader=csv.DictReader(csvfile,delimiter=',')

		for row in reader:
			if InfluenceNode.objects.filter(is_philosopher=True,freebase_id=row['fb1']).all() and InfluenceNode.objects.filter(is_philosopher=True,freebase_id=row['fb2']).all():
				p1 = InfluenceNode.objects.filter(freebase_id=row['fb1']).first()
				p2=InfluenceNode.objects.filter(freebase_id=row['fb2']).first()
				edge=InfluenceEdge(influencer=p1,follower=p2)
				p2.influences.add(p1)
				edge.save()
				p2.save()




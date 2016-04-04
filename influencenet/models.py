from django.db import models

# Create your models here.
class Philosopher(models.Model):
    name=models.CharField(max_length=200)
    date_of_birth=models.DateTimeField(null=True)
    influences=models.ManyToManyField("self", related_name='follower')
    freebase_id=models.CharField(max_length=50,null=True)
    dbpedia_link=models.CharField(max_length=200,null=True)

class InfluenceNode(models.Model):
    name=models.CharField(max_length=200)
    date_of_birth=models.DateTimeField(null=True)
    freebase_id=models.CharField(max_length=50,null=True)
    dbpedia_link=models.CharField(max_length=200,null=True)
    is_philosopher=models.BooleanField(default=False)
    is_writer=models.BooleanField(default=False)

class InfluenceEdge(models.Model):
    influencer=models.ForeignKey(InfluenceNode, related_name='influencer')
    follower=models.ForeignKey(InfluenceNode, related_name='follower')


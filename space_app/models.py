from django.db import models

class Planet(models.Model):
    name = models.TextField()
    desc = models.TextField()
    longest_dist = models.IntegerField()
    shortest_dist = models.IntegerField()
    image = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    item_name = models.TextField()
    length = models.IntegerField()
    item_image = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
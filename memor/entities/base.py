from django.db import models

class Entity(models.Model):
    class Meta:
        proxy = True

from django.db import models

# Create your models here.
class package(models.Model):
    name = models.CharField(null = True,max_length=50)
    description = models.CharField(null = True,max_length=200)
    benefits = models.CharField(null = True,max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

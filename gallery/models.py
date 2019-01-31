from django.db import models

# Create your models here.
class image(models.Model):
    name = models.CharField(null=True,max_length=50)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

from django.db import models

class query(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

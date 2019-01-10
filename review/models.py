from django.db import models

class review(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    rating = models.DecimalField(default=0,max_digits=3,decimal_places=0)
    display = models.DecimalField(default=0,max_digits=3,decimal_places=0,null=True)
    code = models.CharField(max_length=200,default='a')
    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

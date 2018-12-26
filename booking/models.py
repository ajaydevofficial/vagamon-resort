from django.db import models

# Create your models here.
class booking(models.Model):
    booking_id = models.DecimalField(default=0,max_digits=20,decimal_places=0)
    package = models.CharField(default=0,max_length=50,null=False)
    inDate = models.CharField(default=0,max_length=50,null=False)
    outDate = models.CharField(default=0,max_length=50,null=False)
    def __str__(self):
        return str(self.booking_id)
    def __unicode__(self):
        return str(self.booking_id)

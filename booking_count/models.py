from django.db import models

class booking_count(models.Model):
    count = models.DecimalField(default=100,max_digits=50,decimal_places=0)
    
    def __str__(self):
        return str(self.count)

    def __unicode__(self):
        return str(self.count)

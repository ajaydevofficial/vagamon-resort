from django.db import models

BOOKING_STATUS = (
('paid','Paid'),
('unpaid','Unpaid')
)

class booking(models.Model):
    booking_id = models.DecimalField(default=0,max_digits=20,decimal_places=0)
    package = models.CharField(default=0,max_length=50,null=False)
    inDate = models.CharField(default=0,max_length=50,null=False)
    outDate = models.CharField(default=0,max_length=50,null=False)
    status = models.CharField(default='unpaid',max_length=50,null=True,choices=BOOKING_STATUS)
    individuals = models.DecimalField(default=0,max_digits=20,decimal_places=0)
    def __str__(self):
        return str(self.inDate)+'->'+str(self.outDate)
    def __unicode__(self):
        return str(self.inDate)+'->'+str(self.outDate)

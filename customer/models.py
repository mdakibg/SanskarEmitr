from django.db import models

# Create your models here.
class CustomerRecord(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    service = models.CharField(max_length=100)
    subservice = models.CharField(max_length=100)
    payment = models.IntegerField()
    advance = models.IntegerField(default=0)
    priority = models.CharField(max_length=6)
    status = models.CharField(max_length=10, default='Due')
    StatusChanged = models.CharField(max_length=30, default='No change!')
    date = models.DateField(auto_now_add=True, blank=False)

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class LatestUpdate(models.Model):
    headline = models.TextField()
    date = models.DateField(auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.headline} ({self.date})'

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/service', null=True, blank=True)
    isExclusive = models.BooleanField(default=False)
    ExclusiveDescription = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fee = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}({self.fee})'

class UsefulLink(models.Model):
    text = models.CharField(max_length=100)
    url = models.TextField()
    date = models.DateField(auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.text} ({self.url})'
from django.db import models


# Create your models here.
class Booklet(models.Model):
    title=models.CharField(max_length=100,unique=True)
    uploaded=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    file=models.FileField(upload_to='.',null=False,blank=False)
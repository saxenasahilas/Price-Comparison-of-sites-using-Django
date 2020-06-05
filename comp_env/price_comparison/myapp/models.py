from django.db import models

# Create your models here.

#class flipkart(models.Model):
    #fprod=models.CharField(max_length=100)
    #fprice=models.CharField(max_length=100)

#class amazon(models.Model):
    #aprod=models.CharField(max_length=100)
    #aprice=models.CharField(max_length=100)
class amfp(models.Model):
    fprod = models.CharField(max_length=100)
    fprice = models.CharField(max_length=100)
    aprod = models.CharField(max_length=100)
    aprice = models.CharField(max_length=100)
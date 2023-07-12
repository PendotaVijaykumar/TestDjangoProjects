from django.db import models

# Create your models here.
class Movie(models.Model):
    ReleaseDate=models.DateField()
    MovieName=models.CharField(max_length=30)
    Hero=models.CharField(max_length=30)
    Heroine=models.CharField(max_length=30, blank=False) #blank=False means that field is required(*) mandatoryw
    Rating=models.IntegerField ()                           #blank=True means that field is not required i.e optional field

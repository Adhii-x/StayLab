from django.db import models

# Create your models here.

class courses(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class courses1(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class courseCategory(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class form(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name





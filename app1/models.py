from django.db import models

# Create your models here.
class contact(models.Model):
    sno= models.AutoField(primary_key=True)
    email=models.CharField(max_length=50)
    regarding=models.CharField(max_length=40)
    text=models.CharField(max_length=100000000)
    def __str__(self):
        return self.email
class blogpost(models.Model):
    ids=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    catagory=models.CharField(max_length=40)
    title=models.CharField(max_length=40)
    textarea=models.TextField()
    email=models.CharField(max_length=40)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    image=models.ImageField(default='')
    def __str__(self):
        return self.catagory
class appointment(models.Model):
    ids=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    catagory = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    gender = models.TextField()
    email = models.CharField(max_length=40)
    mobile_number= models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
class image(models.Model):
    names=models.CharField(max_length=30)
    images=models.ImageField()







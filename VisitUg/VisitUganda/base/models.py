from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Company Model
class Company(models.Model):
  name = models.CharField(max_length = 255)
  location = models.CharField(max_length=255)
  email = models.EmailField()
  account = models.CharField(max_length=255)
  img = models.ImageField(upload_to='pics')
  mission = models.TextField()
  
# Package Model
class Package(models.Model):
  name = models.CharField(max_length = 255)
  img = models.ImageField(upload_to='pics')
  company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
  description = models.TextField()
  price = models.IntegerField()
  
# Accomodation Model
class Accomodation(models.Model):
  name = models.CharField(max_length=255)
  img = models.ImageField(upload_to='pics')
  location = models.CharField(max_length=255)
  
# Relationship between Package and Accomodation
class PackageAccomodation(models.Model):
  package = models.ForeignKey(Package, null=True, on_delete=models.CASCADE)
  accomodation = models.ForeignKey(Accomodation, null=True, on_delete=models.CASCADE)
  
  
# Transport Model
class Transport(models.Model):
  name = models.CharField(max_length=255)
  img = models.ImageField(upload_to='pics')
  package = models.ForeignKey(Package, default=None, on_delete=models.CASCADE)
  
# Activity Model
class Activity(models.Model):
  name = models.CharField(max_length=255)
  img = models.ImageField(upload_to='pics')
  package = models.ForeignKey(Package, default=None, on_delete=models.CASCADE)
  description = models.TextField()
  
# Comapany Contacts Model
class Contact(models.Model):
  company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
  number = models.CharField(max_length=255)
  
# City Model(cities that can be visited in Uganda)
class City(models.Model):
  name = models.CharField(max_length=255)
  img = models.ImageField(upload_to='pics')
  region = models.CharField(max_length=355)
  description = models.TextField()
    
# Testimonials model
class Testimonial(models.Model):
  username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  img = models.ImageField(upload_to='pics')
  message = models.TextField()
  company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
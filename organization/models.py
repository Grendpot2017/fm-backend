from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

class Photo(models.Model):
    name = models.TextField()
    upload = models.ImageField(upload_to='uploads//%Y/%m/%d/')

class Link(models.Model):
    name = models.CharField(max_length=15)
    url = models.URLField()

class Project(models.Model):
    name = models.CharField(max_length=50)
    links = models.ManyToManyField(Link)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    contact_text = models.CharField(max_length=40)

class Organization(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    url = models.URLField()
    projects = models.ManyToManyField(Project)
    contacts = models.ManyToManyField(Contact)

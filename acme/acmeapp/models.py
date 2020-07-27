from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to='media')

    box_title = models.CharField(max_length=50)
    box_description = models.CharField(max_length=100)
    box_image = models.ImageField(upload_to='media')

    footer = models.CharField(max_length=50)

class About(models.Model):
    about_us = models.CharField(max_length=50)
    info = models.CharField(max_length=500)
    detailed_info = models.CharField(max_length=500)

    our_job = models.CharField(max_length=50)
    job_info = models.CharField(max_length=500)

    footer = models.CharField(max_length=50, default='Acme Web Design, Copyright &copy; 2017')

class Service(models.Model):
    services = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    quote_title = models.CharField(max_length=50)

    footer = models.CharField(max_length=50, default='Acme Web Design, Copyright &copy; 2017')

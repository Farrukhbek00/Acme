from django.db import models

# Create your models here.


class home(models.Model):
    title = models.CharField(max_lenght=50)
    description = models.CharField(max_lenght=100)
    background_image = models.ImageField(upload_to='showcase')

    box_title = models.CharField(max_lenght=50)
    box_description = models.CharField(max_lenght=100)
    box_image = models.ImageField(upload_to='box')

    nav = models.CharField(max_lenght=50)

class about(models.Model):
    about_us = models.CharField(max_lenght=50)
    info = models.CharField(max_lenght=500)
    detailed_info = models.CharField(max_lenght=500)

    our_job = models.CharField(max_lenght=50)
    job_info = models.CharField(max_lenght=500)

class service(models.Model):
    services = models.CharField(max_lenght=50)
    title = models.CharField(max_lenght=50)
    info = models.CharField(max_lenght=50)
    price = models.CharField(max_lenght=50)

    quote_title = models.CharField(max_lenght=50)

# Generated by Django 3.0.8 on 2020-07-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmeapp', '0004_auto_20200726_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='background_image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='home',
            name='box_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmeapp', '0002_auto_20200726_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/', verbose_name='txtImagen'),
        ),
    ]

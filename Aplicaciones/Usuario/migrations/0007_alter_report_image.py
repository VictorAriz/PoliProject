# Generated by Django 4.0.1 on 2022-02-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0006_report_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='Imagenes/', verbose_name='Imagen'),
        ),
    ]

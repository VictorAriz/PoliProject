# Generated by Django 4.0.1 on 2022-02-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_rename_id_user_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
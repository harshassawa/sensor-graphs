# Generated by Django 4.1.7 on 2023-04-04 19:40

from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('django1stapp', '0002_auto_20230405_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_name',
            field= models.CharField(max_length=255, blank=True, null=True),
        ),
    ]

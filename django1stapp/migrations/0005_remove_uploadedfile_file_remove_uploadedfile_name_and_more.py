# Generated by Django 4.1.7 on 2023-04-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django1stapp', '0004_remove_uploadedfile_file_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='file',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='name',
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_1',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_2',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_3',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_4',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_5',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_6',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_7',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_8',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_5',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_6',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name_8',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

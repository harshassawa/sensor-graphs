from django.db import models


# Create your models here.
class UploadedFile(models.Model):
    uploaded_text_files = models.FileField(upload_to='uploads/', max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)



class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')



# from django.db import models
#
# class UploadedFile(models.Model):
#     name_1 = models.CharField(max_length=255)
#     file_1 = models.FileField(upload_to='uploads/')
#     name_2 = models.CharField(max_length=255)
#     file_2 = models.FileField(upload_to='uploads/')
#     name_3 = models.CharField(max_length=255)
#     file_3 = models.FileField(upload_to='uploads/')
#     name_4 = models.CharField(max_length=255)
#     file_4 = models.FileField(upload_to='uploads/')
#     name_5 = models.CharField(max_length=255)
#     file_5 = models.FileField(upload_to='uploads/')
#     name_6 = models.CharField(max_length=255)
#     file_6 = models.FileField(upload_to='uploads/')
#     name_7 = models.CharField(max_length=255)
#     file_7 = models.FileField(upload_to='uploads/')
#     name_8 = models.CharField(max_length=255)
#     file_8 = models.FileField(upload_to='uploads/')
#
#     def __str__(self):
#         return self.name_1

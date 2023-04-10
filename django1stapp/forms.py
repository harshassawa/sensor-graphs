from django import forms
from .models import UploadedFile

class CustomFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        self.filename = kwargs.pop('filename', None)
        super().__init__(*args, **kwargs)

    def save(self, name, content, *args, **kwargs):
        if self.filename:
            name = self.filename
        return super().save(name, content, *args, **kwargs)

# class UploadFileForm(forms.ModelForm):
#     name1 = forms.CharField(required=False)
#     file1 = CustomFileField(required=False)
#
#     name2 = forms.CharField(required=False)
#     file2 = CustomFileField(required=False)
#
#     name3 = forms.CharField(required=False)
#     file3 = CustomFileField(required=False)
#
#     name4 = forms.CharField(required=False)
#     file4 = CustomFileField(required=False)
#
#     name5 = forms.CharField(required=False)
#     file5 = CustomFileField(required=False)
#
#     name6 = forms.CharField(required=False)
#     file6 = CustomFileField(required=False)
#
#     name7 = forms.CharField(required=False)
#     file7 = CustomFileField(required=False)
#
#     name8 = forms.CharField(required=False)
#     file8 = CustomFileField(required=False)
#
#
class UploadFileForm_Pour1(forms.Form):
    name1 = forms.CharField(max_length=255, label="Name 1")
    file1 = CustomFileField(label="File 1")

    name2 = forms.CharField(max_length=255, label="Name 2")
    file2 = CustomFileField(label="File 2")

    name3 = forms.CharField(max_length=255, label="Name 3")
    file3 = CustomFileField(label="File 3")

    name4 = forms.CharField(max_length=255, label="Name 4")
    file4 = CustomFileField(label="File 4")

    name5 = forms.CharField(max_length=255, label="Name 5")
    file5 = CustomFileField(label="File 5")

    name6 = forms.CharField(max_length=255, label="Name 6")
    file6 = CustomFileField(label="File 6")

    name7 = forms.CharField(max_length=255, label="Name 7")
    file7 = CustomFileField(label="File 7")

    name8 = forms.CharField(max_length=255, label="Name 8")
    file8 = CustomFileField(label="File 8")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 9):
            self.fields[f'name{i}'].widget.attrs.update({'class': 'form-control'})
            self.fields[f'file{i}'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = UploadedFile
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        for i in range(1, 9):
            name_field = 'name{}'.format(i)
            file_field = 'file{}'.format(i)
            name = cleaned_data.get(name_field)
            file = cleaned_data.get(file_field)
            if name and not file:
                self.add_error(file_field, 'Please select a file for {}.'.format(name))
            elif file and not name:
                self.add_error(name_field, 'Please enter a name for the selected file.')
        return cleaned_data

class UploadFileForm_Pour2(forms.Form):
    name1 = forms.CharField(max_length=255, label="Name 1")
    file1 = CustomFileField(label="File 1")

    name2 = forms.CharField(max_length=255, label="Name 2")
    file2 = CustomFileField(label="File 2")

    name3 = forms.CharField(max_length=255, label="Name 3")
    file3 = CustomFileField(label="File 3")

    name4 = forms.CharField(max_length=255, label="Name 4")
    file4 = CustomFileField(label="File 4")

    name5 = forms.CharField(max_length=255, label="Name 5")
    file5 = CustomFileField(label="File 5")

    name6 = forms.CharField(max_length=255, label="Name 6")
    file6 = CustomFileField(label="File 6")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 7):
            self.fields[f'name{i}'].widget.attrs.update({'class': 'form-control'})
            self.fields[f'file{i}'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = UploadedFile
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        for i in range(1, 7):
            name_field = 'name{}'.format(i)
            file_field = 'file{}'.format(i)
            name = cleaned_data.get(name_field)
            file = cleaned_data.get(file_field)
            if name and not file:
                self.add_error(file_field, 'Please select a file for {}.'.format(name))
            elif file and not name:
                self.add_error(name_field, 'Please enter a name for the selected file.')
        return cleaned_data
from django import forms
from timezone_field.forms import TimeZoneFormField
from easy_thumbnails.widgets import ImageClearableFileInput


class UserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    timezone = TimeZoneFormField()
    gender = forms.ChoiceField(choices=(
        (1, "Мужчина"),
        (2, "Женщина"),
    ))
    birth_date = forms.DateField()
    about = forms.CharField(widget=forms.Textarea)
    photo = forms.FileField(widget=ImageClearableFileInput)
    background = forms.FileField(widget=ImageClearableFileInput)


class StatusForm(forms.Form):
    status = forms.CharField()
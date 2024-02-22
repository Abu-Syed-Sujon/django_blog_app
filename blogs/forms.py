from django import forms
from django.core import validators

class TeacherRegistration(forms.Form):
    'teacher registration form'
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=10)
    email = forms.EmailField(label="Enter Email")
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.FileInput)  # for creating file input

    def clean(self):
        cleaned_data = super().clean()
        first_pass = cleaned_data.get('password')
        second_pass = cleaned_data.get('repassword')
        if first_pass and second_pass and first_pass != second_pass:
            raise forms.ValidationError('Passwords do not match')

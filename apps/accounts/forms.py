from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.Form):
    mobile = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "موبایل",
                "class": "form-control"
            }
        ))
    
    
    postal_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کدپستی",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "شهر",
                "class": "form-control"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "کشور",
                "class": "form-control"
            }
        ))
  
    birthday = forms.DateField(
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                "placeholder": "تاریخ تولد",
                "class": "form-control",
                "type": "date"
            }
        )
    )
 
    father_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام پدر",
                "class": "form-control"
            }
        )
    )
    mother_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام مادر",
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "آدرس",
                "class": "form-control"
            }
        )
    )
    upload_img = forms.ImageField(required=False)
   

    class Meta:
        model = Profile ,
        fields = ('mobile', 'postal_code', 'city', 'country', 'birthday', 'father_name', 'mother_name', 'address', 'upload_img')

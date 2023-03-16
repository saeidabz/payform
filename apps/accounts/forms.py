from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.Form):
    first_name = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام",
                "class": "form-control"
            }
        ))
    
    last_name = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام خانوادگی",
                "class": "form-control"
            }
        ))
    
    code_melli = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کد ملی",
                "class": "form-control"
            }
        ))
    
    mobile = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "شماره همراه",
                "class": "form-control"
            }
        ))
    
    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "شماره ثابت",
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
    
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "شهر",
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
    
    postal_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کدپستی",
                "class": "form-control"
            }
        ))
    
    
  
    
   

    class Meta:
        model = Profile ,
        fields = ('first_name', 'last_name', 'code_melli', 'mobile', 'phone', 'country', 'city', 'birthday', 'father_name', 'mother_name', 'address', 'postal_code', )

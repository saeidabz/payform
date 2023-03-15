from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام خانوادگی"
            }
        )
    )
    national_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کد ملی"
            }
        )
    )
    mobile_number = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "شماره موبایل"
            }
        )
    )
    fixed_number = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "تلفن ثابت"
            }
        )
    )
    country = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کشور"
            }
        )
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "شهر"
            }
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "تاریخ تولد"
            }
        )
    )
    father_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام پدر"
            }
        )
    )
    mother_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام مادر"
            }
        )
    )
    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "آدرس"
            }
        )
    )
    postal_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "کد پستی"
            }
        )
    )
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'national_code', 'mobile_number', 'fixed_number', 'country', 'city', 'date_of_birth', 'father_name', 'mother_name', 'address', 'postal_code', 'username', 'email', 'password1', 'password2')

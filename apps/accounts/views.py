from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile
import string
import random
from django.template.loader import get_template

def success_view(request, user_id):
    print(user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'accounts/download_pdf.html', {'user': user, 'logout': 'logout'})


def insert_profile(request):
    form = ProfileForm(request.POST)
    msg = None
    success = False
    if form.is_valid():
        username = form.cleaned_data.get('mobile')
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        user = User.objects.create_user(
            username=username, 
            first_name=form.cleaned_data.get('first_name'), 
            last_name=form.cleaned_data.get('last_name'),
            email="e"+username+"@gmail.com", 
            password=password
            )

        profile = Profile.objects.create(
            user=user, 
            mobile=form.cleaned_data.get("mobile"), 
            phone=form.cleaned_data.get("phone"), 
            code_melli=form.cleaned_data.get("code_melli"),
            postal_code=form.cleaned_data.get("postal_code"),
            city=form.cleaned_data.get("city"),
            country=form.cleaned_data.get("country"),
            birthday=form.cleaned_data.get("birthday"),
            father_name=form.cleaned_data.get("father_name"),
            mother_name=form.cleaned_data.get("mother_name"),
            address=form.cleaned_data.get("address"),
        )

        return redirect('success', user_id=user.id)
        
    else:
        return render(request, "accounts/profile.html", {"form": form, "msg": msg, "success": success})

def submit_form(request):
    form = ProfileForm()
    return render(request, "accounts/profile.html", {"form": form})


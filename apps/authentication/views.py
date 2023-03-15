from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def insert_user(request):
    form = SignUpForm(request.POST)
    msg = None
    success = False
    if form.is_valid():
        user = form.save()
        user.profile.mobile = form.cleaned_data.get("mobile")
        user.profile.postal_code = form.cleaned_data.get("postal_code")
        user.profile.save() # Save the Profile model instance
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)

        # Generate the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="user_info_{username}.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response)

        # Write the user's information to the PDF file.
        user_info = f"Username: {username}\nEmail: {user.email}\n"
        p.drawString(100, 750, user_info)

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        # Return the response.
        return render(request, "accounts/download_pdf.html", {"form": form, "msg": msg, "success": True})

    else:
        return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def register_user(request):
    form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form})


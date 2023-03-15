from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile
import string
import random
# from xhtml2pdf import pisa
# import io
# from django.http import FileResponse
from django.template.loader import get_template

# def generate_pdf(request, user_id):
#     # id = 69
#     # print(user_id)
#     # print("dasdasdsaasdsad")
#     user = User.objects.get(pk=user_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="user_info_{user.username}.pdf"'

#     template_path = 'accounts/pdf.html'
#     context = {'user': user}
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="user_info_{user_id}.pdf"'

#     template = get_template(template_path)
#     html = template.render(context)

#     pisa.CreatePDF(html, dest=response)

#     return response

# import tempfile
# from weasyprint import HTML
# from weasyprint import CSS
# from weasyprint.fonts import FontConfiguration

# def generate_pdf(request, user_id):
#     user = User.objects.get(pk=user_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="user_info_{user.username}.pdf"'

#     template_path = 'accounts/pdf.html'
#     context = {'user': user}

#     template = get_template(template_path)
#     html = template.render(context)

#     with tempfile.NamedTemporaryFile(delete=False) as tmp:
#         tmp.write(html.encode('utf-8'))
#         tmp.seek(0)

#         pdf = HTML(tmp.name).write_pdf(
#             stylesheets=[CSS(string='@font-face { font-family: "IranSans"; src: url(/path/to/IRANSansWeb.ttf) }')],
#             font_config=FontConfiguration(),
#             presentational_hints=True,
#             encoding='utf-8'
#         )

#     response.write(pdf)
#     return response





def insert_profile(request):
    form = ProfileForm(request.POST, request.FILES)
    msg = None
    success = False
    if form.is_valid():
        username = form.cleaned_data.get('mobile')
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        user = User.objects.create_user(username=username, email="e"+username+"@gmail.com", password=password)

        profile = Profile.objects.create(
            user=user, 
            mobile=form.cleaned_data.get("mobile"), 
            postal_code=form.cleaned_data.get("postal_code"),
            city=form.cleaned_data.get("city"),
            country=form.cleaned_data.get("country"),
            birthday=form.cleaned_data.get("birthday"),
            father_name=form.cleaned_data.get("father_name"),
            mother_name=form.cleaned_data.get("mother_name"),
            address=form.cleaned_data.get("address"),
            upload_img=request.FILES.get("image") # Retrieve uploaded image
        )

        return render(request, "accounts/download_pdf.html", {"form": form, "msg": msg, "success": success, "user": user})
        
    else:
        return render(request, "accounts/profile.html", {"form": form, "msg": msg, "success": success})

def submit_form(request):
    form = ProfileForm()
    return render(request, "accounts/profile.html", {"form": form})


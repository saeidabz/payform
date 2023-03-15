
from django.shortcuts import render
from django.http import HttpResponse

from saeidtest.models import User
from saeidtest.utils import render_to_pdf
from .forms import UserForm
from django.views.generic import View
from django.template.loader import get_template
from xhtml2pdf import pisa

class UserRegistration(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'saeidtest.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponse('User created successfully')
        return render(request, 'test/register.html', {'form': form})

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('register/pdf.html')
        context = {'user': User.objects.get(id=kwargs['pk'])}
        html = template.render(context)
        pdf = render_to_pdf('test/pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "User_%s.pdf" % context['user'].username
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")

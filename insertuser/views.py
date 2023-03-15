from django.shortcuts import render
from .forms import SignUpForm

def sample_view(request):
    form = SignUpForm()
    return render(request, 'sample.html', {'form': form})
from django.shortcuts import render
# Create your views here.

from .forms import Number2
from django.views.generic import TemplateView

# Create your views here.

def homeGet(request):
    return render(request,'CalculaterGet.html')

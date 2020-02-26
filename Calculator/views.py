from django.shortcuts import render
from .forms import Number
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'home.html',{'form' : Number})

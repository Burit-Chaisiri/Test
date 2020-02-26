from django.shortcuts import render
from .forms import Number
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    if request.method == 'POST':
        form=Number(request.POST)
        
        if form.is_valid():
            text = form.cleaned_data['x']
            text2 = form.cleaned_data['y']
            
            if 'add' in request.POST:
                result = text + text2
            elif 'sub' in request.POST:
                result = text - text2
            elif 'mul' in request.POST:
                result = text * text2
            elif 'div' in request.POST:
                result = text / text2    
            form = Number()
        args = {'form': form , 'result': result}
        return render(request, 'home.html', args )    
    else:  
        form=Number()
    return render(request,'home.html',{'form':form})

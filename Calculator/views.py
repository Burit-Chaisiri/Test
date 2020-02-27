from django.shortcuts import render
from .forms import Number
from django.views.generic import TemplateView
#from .models import Calculate
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def Calculator(request):
    if request.method == 'POST':
        form=Number(request.POST)   
        if form.is_valid():
            text = form.cleaned_data['x']
            text2 = form.cleaned_data['y']

            if 'add' in request.POST:
                result = text + text2
                op='add'
            elif 'sub' in request.POST:
                result = text - text2
                op='sub'
            elif 'mul' in request.POST:
                result = text * text2
                op='mul'
            elif 'div' in request.POST:
                result = text / text2
                op='div'   

            form = Number()
        
        args = {'form': form , 'result': result}
      #  Calculate.objects.create(expression =str(text)+op+str(text2),answer = str(result))
       # History=Calculate.objects.all()
        return render(request, 'Calculator.html', args )    
    else:  
        form=Number()
    return render(request,'Calculator.html',{'form':form})


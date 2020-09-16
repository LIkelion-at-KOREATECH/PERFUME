from django.shortcuts import render

# Create your views here.
def choose(request):
    return render(request,'choose.html')

def choose_atm(request):
    return render(request, 'choose_atm.html')

def choose3(request):
    return render(request,'choose3.html')
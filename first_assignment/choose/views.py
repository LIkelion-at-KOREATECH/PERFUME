from django.shortcuts import render

# Create your views here.
def choose(request):
    return render(request,'choose.html')
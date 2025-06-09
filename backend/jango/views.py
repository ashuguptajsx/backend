from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.

def all_jango(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'jango/all_jango.html',{'chais':chais})

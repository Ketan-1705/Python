

# Create your views here.
from django.shortcuts import render

def home(request):
    data = {
        'name': 'Kinjal'
    }
    return render(request, 'index.html', data)
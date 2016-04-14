from datetime import datetime

from django.shortcuts import render

def home(request):
    return render(request, 'home2.html', {'right_now':datetime.utcnow()})
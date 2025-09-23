from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # quick text response:
    return HttpResponse("✅ Complaint System skeleton is up — Hello FRANESH!")
    # or render a template:
    # return render(request, 'index.html')

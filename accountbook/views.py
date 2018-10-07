from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    msg = "JB"
    return render(request, 'accountbook_index.html', {'message': msg})
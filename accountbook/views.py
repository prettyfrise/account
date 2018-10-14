from django.shortcuts import render

def index(request):
    msg = "JB"
    return render(request, 'accountbook_content.html', {'message': msg})
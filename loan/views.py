from django.shortcuts import render
from expense.models import MobelTable
from django.utils import timezone


def loan_main(request):
    if request.POST.get("your name"):
        msg = request.POST['your name']
    else:
        msg = "NO"
    template = 'loan/loan_main.html'
    return render(request, template, {'msg': msg})

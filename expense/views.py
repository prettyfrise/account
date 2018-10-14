from django.shortcuts import render
from expense.models import MobelTable
from django.utils import timezone

def expense_home(request):
    template = 'expense/expense_index.html'
    return render(request, template)


def expense_input(request):
    template = 'expense/expense_record.html'

    return render(request, template)


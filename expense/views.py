from django.shortcuts import render

def expense_home(request):
    template = 'expense/expense_index.html'
    return render(request, template)


def expense_input(request):
    template = 'expense/expense_record.html'
    return render(request, template)


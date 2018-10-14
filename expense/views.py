from django.shortcuts import render

def expense_home(request):
    template = 'expense/expense_index.html'
    context = dict(msg = "JB")

    return render(request, template, context)


def expense_input(request):
    template = 'expense/expense_record.html'
    context = dict(msg = "JB")

    return render(request, template, context)
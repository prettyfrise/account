from django.shortcuts import render
from expense.models import MobelTable
from django.utils import timezone

def expense_home(request):
    p = MobelTable.objects.all()

    template = 'expense/expense_index.html'
    return render(request, template, {'p':p})


def expense_input(request):
    if request.POST:
        category = request.POST['category']
        usedate = request.POST['usedate']
        field = request.POST['field']
        Subscribe = request.POST['Subscribe']
        price = request.POST['price']
        payment_logic = request.POST['payment_logic']
        etc = request.POST['etc']
        p = MobelTable(usedate=usedate, category=category,field=field,subscribe=Subscribe, price=price,payment_logic=payment_logic,etc=etc)
        p.save()
    else:
        category = ''
        usedate = ''
        field = ''
        Subscribe = ''
        price =''
        payment_logic =''
        etc =''
    template = 'expense/expense_record.html'
    return render(request, template, {'category': category,
                                      'usedate': usedate,
                                      'field': field,
                                      'Subscribe': Subscribe,
                                      'price': price,
                                      'payment_logic': payment_logic,
                                      'etc': etc})

#
#
#
# def loan_main(request):
#     if request.POST.get("your name"):
#         msg = request.POST['your name']
#     else:
#         msg = "NO"
#     template = 'loan/loan_main.html'
#     return render(request, template, {'msg': msg})
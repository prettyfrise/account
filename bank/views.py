from django.shortcuts import render

def bankinfo_list(request):

    template = 'bank/bankinfo_list.html'
    return render(request, template)

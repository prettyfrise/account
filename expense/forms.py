from django import forms
import datetime

class ExpenseForms(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    usedate = forms.DateField(initial=datetime.date.today)
    category = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)
    subscribe = forms.CharField(max_length=100)
    price = forms.IntegerField(max_value=0)
    payment_logic = forms.CharField(max_length=30)
    etc = forms.CharField(max_length=100)


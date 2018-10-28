from django import forms
import datetime

class ExpenseForms(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    usedate = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'class' : 'date-picker',
                                                                                         'autocomplete' : 'off',
                                                                                         'placeholder' : '날짜선택'}))
    category = forms.CharField(max_length=30)
    field = forms.CharField(max_length=30)
    subscribe = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    price = forms.IntegerField(max_value=0, widget=forms.TextInput(attrs={'class' : 'form-control',
                                                                          'placeholder' : '1,000,000',
                                                                          'autocomplete' : 'off'}))
    payment_logic = forms.CharField(max_length=30)
    etc = forms.CharField(max_length=100)


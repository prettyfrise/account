from django import forms
import datetime


class ExpenseForms(forms.Form):

    CHOICES2 = (('급여', '급여',),
                ('인센', '인센'),
                ('기타', '기타'))


    CHOICES3 = (('자동이체', '자동이체'),
                ('현금', '현금'))

    usedate = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'class': 'date-picker',
                                                                                         'autocomplete': 'off',
                                                                                         'placeholder': '날짜선택'}))
    category = forms.CharField(max_length=30)
    field = forms.ChoiceField(choices=CHOICES2, widget=forms.Select(attrs={'class': 'form-control'}))
    subscribe = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(max_value=0, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': '1,000,000',
                                                                          'autocomplete': 'off'}))

    payment_logic = forms.ChoiceField(choices=CHOICES3, widget=forms.Select(attrs={'class': 'form-control'}))
    etc = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': '할인/적립 기타 등등',
                                                                        'autocomplete': 'off'}))

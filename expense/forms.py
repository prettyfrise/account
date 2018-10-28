from django import forms
import datetime


class ExpenseForms(forms.Form):
    # TODO 나중에 DB에서 목록을 가져오도록 수정
    CHOICES2 =(('급여', '급여'),
               ('인센', '인센'),
               ('기타', '기타'),
               )

    # TODO 나중에 DB에서 목록을 가져오도록 수정
    CHOICES3 =(('자동이체', '자동이체'),
               ('현금', '현금'),
               )


    # your_name = forms.CharField(label='Your name', max_length=100)
    usedate = forms.DateField(initial=datetime.date.today)
    field = forms.ChoiceField(choices=CHOICES2, widget=forms.Select(attrs={'class' : 'form-control'}))
    subscribe = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    price = forms.IntegerField(max_value=0)
    payment_logic = forms.ChoiceField(choices=CHOICES3, widget=forms.Select(attrs={'class' : 'form-control'}))
    etc = forms.CharField(max_length=100)

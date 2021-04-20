from .models import Budget, Money, Famdetails
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Famdetails
        fields = [
        "profile_pic",
        "role",
        "age",
        "salary",
        ]



class MoneyForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Money
        fields = [
            "name",
            "savingPer",
            "wantPer",
            "needPer",
            "publish",
        ]

class BudgetForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Budget
        fields = [
            "itemname",
            "amount",
            "category",
            #"publish",
        ]

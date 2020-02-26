from django import forms
class Number(forms.Form):
    x = forms.IntegerField(required=False)
    y = forms.IntegerField(required=False)
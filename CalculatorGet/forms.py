from django import forms
class Number2(forms.Form):
    x = forms.IntegerField(required=False)
    y = forms.IntegerField(required=False)
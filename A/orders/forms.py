from django import forms

class CartAddform(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9)


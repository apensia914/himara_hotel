from django import forms 

class ShopSearchForm(forms.Form):
    name = forms.CharField()
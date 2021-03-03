from django import forms 

class SearchForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
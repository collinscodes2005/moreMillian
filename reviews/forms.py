from django import forms 

class NameForm(forms.Form):
    name = forms.CharField(label = "Username", max_length=100)
    review = forms.CharField(label = "Your review", widget=forms.Textarea, max_length=200)
    
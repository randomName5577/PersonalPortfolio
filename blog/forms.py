from django import forms
from django.core import validators


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment!'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email to get notified of a response'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
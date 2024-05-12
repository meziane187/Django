from django import forms


class InputForm(forms.Form):
    x=forms.IntegerField(label="Enter you first number")
    y=forms.IntegerField(label="Enter you second number")

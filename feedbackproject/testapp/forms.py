from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name=forms.CharField()
    roolnum=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)


    def clean(self):
        total_cleaned_data=super().clean()
        inpname=total_cleaned_data['name']
        if len(inpname)<4:
            raise forms.ValidationError("name shoul b atleast 4 characters")
        inpfeedback=total_cleaned_data['feedback']
        if len(inpfeedback)<=40:
            raise forms.ValidationError("Feedback atleast 40 characters")
        inprollnum=total_cleaned_data['roolnum']
        if inprollnum<0:
            raise forms.ValidationError("Rool num must be > 1")

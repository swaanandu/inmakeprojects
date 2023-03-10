from django import forms

from todoapp.models import Todo


class todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['task','priority']
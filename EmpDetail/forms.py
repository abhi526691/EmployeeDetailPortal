from django.db import models
from .models import Employee
from django import forms
from django.forms import ModelForm, fields

class EmployeeDetail(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['TTS_No'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your TTS_No', 'type':'Number'})
        self.fields['Name'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Name', 'type':'text'})
        self.fields['Email'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Email', 'type':'email'})
        self.fields['Age'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Age', 'type':'Number'})
        self.fields['Gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['Designation'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Designation', 'type':'text'})
        self.fields['Batch'].widget.attrs.update({'class': 'form-control'})
        self.fields['Branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['Prev_Company'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Previous Company', 'type':'text'})
        self.fields['Prev_Exp_Year'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Year Of Experience', 'type':'Number'})
        self.fields['Date_of_Joining'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['Date_of_Birth'].widget.attrs.update({'class': 'form-control', 'type':'date'})

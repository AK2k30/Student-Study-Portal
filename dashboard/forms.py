from django import forms
from .models import ass
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']
        
class DateInput(forms.DateInput):
    input_type = 'date'
        
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']
        
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter your search: ")
    
    
class AssignForm(forms.ModelForm):
    class Meta:
        model = ass
        fields = ('title','owner','pdf', 'cover')
    
    
class ExpForm(forms.ModelForm):
    class Meta:
        model = exx
        fields = ('title','owner','pdf', 'cover')
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    Semester = forms.CharField(max_length=100)
    Branch = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','Semester','Branch']
        labels = {'email':'Email'}
        
    
        



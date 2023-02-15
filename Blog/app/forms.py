from .models import Blog,Profile,Comment
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



   
class CreateUser(UserCreationForm):
   class Meta:
      model=User
      fields=['username','email','password1','password2']

class CreateProfile(ModelForm):
    class Meta:
      model=Profile
      fields=['state','country']



class CreateBlog(ModelForm):
   title=forms.CharField(widget=forms.TextInput(attrs={
       "class":"text_design",
       "type":"text",
   }))
   class Meta:
      model=Blog
      fields=['title','description']


class UpdateUser(ModelForm):
   username=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   
   class Meta:
      model=User
      fields=['username']



class UpdateProfile(ModelForm):
   mobileno=forms.IntegerField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   country=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   state=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   email=forms.EmailField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   surname=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
       "type":"text",
   }))
   class Meta:
      model=Profile
      fields=['image','email','country','state','surname','mobileno']

class CommentForm(ModelForm):
   class Meta:
      model=Comment
      fields=['body']

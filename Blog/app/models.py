from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   date=models.DateField(default=timezone.now)
   title=models.CharField(max_length=100)
   description=RichTextField(null=True,blank=True)
   likes=models.ManyToManyField(User,related_name='likeup')

   def total_like(self):
      return self.likes.count()

   def __str__(self):
      return self.title


class Profile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
   name=models.CharField(max_length=100,null=True)
   surname=models.CharField(max_length=100,null=True)
   mobileno=models.IntegerField(default=91)
   email=models.EmailField(null=True)
   country=models.CharField(max_length=30,null=True)
   state=models.CharField(max_length=30,null=True)
   image=models.ImageField(default='default.png',upload_to='profile_pics')

   def __self__(self):
      return f'{self.user.username} Profile'

class Comment(models.Model):
   post=models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
   author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   date_added=models.DateTimeField(default=timezone.now)
   body=models.CharField(max_length=200,blank=True,null=True)


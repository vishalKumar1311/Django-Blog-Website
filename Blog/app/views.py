from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from .models import Blog,Comment,Profile
from .forms import CreateBlog,UpdateUser,CreateUser,CreateProfile,UpdateProfile,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def Home(request):
   q=request.GET.get('q') if request.GET.get('q')!=None else ''
   sblog=Blog.objects.filter(description__icontains=q)
   blog=Blog.objects.all()
   context={
      'blog':blog,
      'sblog':sblog
   }

   return render(request,'app/home.html',context)

def createBlog(request):
   form=CreateBlog()
   if request.method=='POST':
      form=CreateBlog(request.POST)
      if form.is_valid():
         form.instance.user=request.user
         form.save()
         return redirect('home')

   return render(request,'app/create.html',context={ 'form':form})      

def deleteBlog(request,id):
   Blog.objects.get(pk=id).delete()
   return redirect('home')

def updateBlog(request,id):
   blog=Blog.objects.get(id=id)
   form=CreateBlog(instance=blog)
   if request.method=='POST':
      form=CreateBlog(request.POST,instance=blog)
      if form.is_valid:
         form.save()
         return redirect('home')
   return render(request, 'app/update.html',context={"form":form})      
      

def loginBlog(request):
   print("sada")
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      print("check")
      user=authenticate(request,username=username,password=password)

      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Invalid Credentials')

   return render(request,'app/login.html')
   


def registerBlog(request):
   form=CreateUser()
   form2=CreateProfile()
   if request.method=='POST':
      form=CreateUser(request.POST)
      form2=CreateProfile(request.POST)
      print(request.POST.get('state'))
      if form.is_valid() and form2.is_valid():
         b = Profile(user=request.user,state=request.POST.get('state'), country=request.POST.get('country'))
         b.save()
         # form.save()
         return redirect('login')
   
   return render(request,'app/register.html',{'form':form,'form2':form2})


@login_required
def profile(request):
   if request.method=='POST':
      uform=UpdateUser(request.POST,instance=request.user)
      uimg=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
      if uform.is_valid() and uimg.is_valid():
         uform.save()
         uimg.save()
         return redirect('profile')
   else:
      uform=UpdateUser(instance=request.user)
      uimg=UpdateProfile(instance=request.user.profile)
   
   context={
      'uform':uform,
      'uimg':uimg
   }
   return render(request,'app/profile.html',context)




def userContent(request,user):
   data=User.objects.get(username=user)
   print(data)
   blog=Blog.objects.filter(user=data)
   context={
      'blog':blog
   }

   return render(request,'app/detail.html',context)


def specificPost(request,id):
   blog=Blog.objects.filter(pk=id)
   lcount=get_object_or_404(Blog, pk=id)
   print(lcount)
   count=lcount.total_like()
   cform=CommentForm()
   commentshow=Comment.objects.all()
   context={
      'blog':blog,
      'commentshow':commentshow,
      'cform':cform,
      'count':count
   }
   return render(request,'app/detail.html',context)




def addComment(request,id):
   cform=CommentForm()
   if request.method=='POST':
     cform=CommentForm(request.POST)
     if cform.is_valid():
      print("Hello")
      cout=cform.save(commit=False)
      cout.author=request.user
      cout.post=Blog.objects.get(pk=id)
      cout.save()
      return HttpResponseRedirect(reverse('userspecific',args=[id]))
   
   return render(request,'app/detail.html')


def addLike(request,id):
   if request.method=='POST':
      blog=Blog.objects.get(pk=id)
      blog.likes.add(request.user)
      print("Hello")
      return HttpResponseRedirect(reverse('userspecific',args=[id]))
   
   return render(request,'app/detail.html')


def logout_view(request):
   logout(request)
   return render(request,'app/home.html')

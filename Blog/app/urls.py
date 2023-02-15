from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('create/', views.createBlog ,name='create'),
    path('update/<int:id>', views.updateBlog,name='update'),
    path('delete/<int:id>', views.deleteBlog,name='delete'),
    path('login/', views.loginBlog,name='login'),
     path('logout/', views.logout_view,name='logout'),
    path('register/', views.registerBlog,name='register'),
    path('profile/', views.profile,name='profile'),
    path('userprofile/<str:user>', views.userContent,name='userprofile'),
    path('userspecific/<int:id>', views.specificPost,name='userspecific'),
    path('<int:id>/comment', views.addComment,name='comment'),
    path('<int:id>/like', views.addLike,name='like'),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login

def index(request):
	blogs = BlogArticle.objects.all()
	if request.method == "POST": 
			usname = request.POST['username']
			pwd = request.POST['password']
			user = authenticate(username=usname, password=pwd)
			if user is not None: 
				login(request, user)
				return render(request, "main.html", {'testvar': "test string 2", "blogs": blogs, "user": user})
	return render(request, "main.html", {'testvar': "test string 2", "blogs": blogs, "user": None})

def createBlog(request):
	newBlog = BlogArticle()
	newBlog.title = request.Post['title']
	newBlog.author = request.user
	newBlog.blog_content = request.Post['blog_content']
	newBlog.save()
	return render(request, "main.html", {'testvar': "test string 2", "blogs": blogs, "user": user})
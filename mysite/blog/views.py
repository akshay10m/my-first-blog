from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
from django.utils import timezone


def post_list(request):
	posts = Post.objects.filter(date_created__lte=timezone.now()).order_by('date_published')
	return render(request,'blog/post_list.html',{'posts':posts})

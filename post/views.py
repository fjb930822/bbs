# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from math import ceil

from django.shortcuts import render, redirect

from post.models import Post
from post.helper import page_cache, read_count
from post.helper import get_top_n

# Create your views here.

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    return render(request,'create_post.html')


def edit_post(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(id=post_id)
        return render(request,'edit_post.html',{'post':post})


@read_count
@page_cache(2)
def read_post(request):
    post_id =int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    return render(request,'read_post.html',{'post':post})


def post_list(request):
    page = int(request.GET.get('page',1))
    per_page = 10
    post = Post.objects.count()
    pages = ceil(post / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.all()[start:end]
    return render(request,'post_list.html',{'posts':posts, 'pages':range(pages)})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request,'search.html',{'posts':posts})

def top10(request):
    rank_data = get_top_n(10)
    return render(request,'top10.html',{'rank_data':rank_data})
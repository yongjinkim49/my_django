# blogPosts/views.py
from django.shortcuts import render, redirect # redirect 추가
from .models import Post
...
# index 함수 코드 변경
def index(request):
    if request.method == 'GET': # index
        posts = Post.objects.all()
        return render(request, 'blogPosts/index.html', {'posts': posts})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('blogPosts:index')
...

def new(request):
    return render(request, 'blogPosts/new.html')

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogPosts/show.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('blogPosts:index')
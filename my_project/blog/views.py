from django.shortcuts import render
from blog.forms import *
from blog.models import *
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
    return render(request, 'home.html')

def browser(request):
    form = Article_name()
    result = {}
    if 'submit' in request.POST:
        try:
            blog = list(blogs.objects.filter(article_name=
                                             request.POST['article_name']).values('article_name','plain_text'))
        except Exception as e:
            raise e
        if blog:
            result['title'] = blog[0]['article_name']
            result['content'] = blog[0]['plain_text']

            return render(request, 'result2.html', {'form': result})



    return render(request, 'browser.html',{'form':form})

def posts(request):
    form = Post_new()
    if request.POST:
        f = Post_new(request.POST)
        if f.is_valid():
            if 'submit' in request.POST:
                blog = blogs()
                blog.article_name = request.POST['title']
                blog.plain_text = request.POST['plain']
                try:
                    blog.save()
                    return render(request, 'result.html', {'form': 'Post successfully'})
                except Exception as e:
                    raise e
        else:
            return render(request, 'result2.html', {'form': 'The article has been posted, please change another name'})
    return render(request, 'post.html',{'form':form})
from django.shortcuts import render
from .models import BlogArticles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BlogArticlesForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # new

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    page_size = 2
    paginator = Paginator(blogs, page_size)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    current_blogs = current_page.object_list
    return render(request, 'blog/titles.html', {'blogs': current_blogs, 'page': current_page})

def blog_article(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    return render(request, 'blog/content.html', {'article': article})

@login_required()
def blog_post(request):
    if request.method == 'GET':
        blog_form = BlogArticlesForm()
        return render(request, 'blog/blog_post.html', {'blog_form': blog_form})

    if request.method == 'POST':
        blog_form = BlogArticlesForm(request.POST)
        # 表单数据验证通过
        if blog_form.is_valid():
        	# 获取表单数据
            cd = blog_form.cleaned_data
            try:
                new_blog = blog_form.save(commit=False)
                new_blog.author = request.user
                new_blog.save()
                return HttpResponse('1')
            except Exception as e:
                return HttpResponse('-1')
        else:
            return HttpResponse('0')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed

def index(request):
    articles = Article.objects.all() #articles에 전체 목록을 다 가져옴
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    """
    Form Class
    1. 모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 정제 후 DB에 실제 저장하는 로직 필요

    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음
    form.save()만 해도 DB에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다
        form = ArticleForm(request.POST)
        # 해당 form이 유효한지 확인
        if form.is_valid():
            # # form.cleaned_data를 통해 form 데이터를 정제한다. (form.cleaned_data == Dictionary)
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            # embed()
            article = form.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk): # urls 파일에 따라서 인자 이름 정하면 됨.
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index') # redirect -> GET 요청
    else:
        return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # instance-> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            # embed()
            form.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance = article)
        # embed()
    context = {'form': form, 'article': article, }
    return render(request, 'articles/form.html', context)

"""
* CREATE & UPDATE는 html 파일 공유 (차이 꼭 알아두기!)
Create 로직
1. GET
- 사용자가 데이터를 입력할 수 있는 빈 Form을 제공
2. POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1. GET
- 기존 사용자의 글이 입력된 Form 제공
2. POST
- 수정된 글을 DB에 저장
"""

def comments_create(request, article_pk):
    if request.method == 'POST':
        comment_form = CommentFrom(request.POST)
        ...
        comment = commit_form.save(commit=False)
        ...
        comment.save()
    return redirect('articles:detail', article_pk)
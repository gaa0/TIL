from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    # embed()
    # 1. session 정보에서 visits_num이라는 키로 접근해 값을 가져옴.
    # 해당하는 키가 없으면 0을 가져옴.
    visits_num = request.session.get('visits_num', 0)
    # 2. 가져온 값을 session에 'visits_num'이라는 새로운 키의 값으로 1씩 증가.
    request.session['visits_num'] = visits_num + 1
    # 3. session data를 수정하면 장고는 수정한 내용을 알 수 없어서 작성하는 코드
    request.session.modified = True
    # embed()

    articles = Article.objects.all() #articles에 전체 목록을 다 가져옴
    context = {
        'articles': articles, 'visits_num': visits_num,
    }
    return render(request, 'articles/index.html', context)

@login_required
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
    # article_form = ArticleForm()
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index') # redirect -> GET 요청
    # return redirect('articles:detail', article.pk)

@login_required
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

@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):  # urls.py에 종속됨
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
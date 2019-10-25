from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article, 'comment_form': comment_form, 'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article_pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form':article_form, 
    }
    return render(request, 'articles/update.html', context)

def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)
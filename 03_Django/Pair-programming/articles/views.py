from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles 
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        articles = Article()
        articles.title = title
        articles.content = content
        articles.save()
        return redirect("articles:index")
    else:
        return render(request, 'articles/create.html')

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    context = {
        'article': article, 
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        return redirect("articles:detail", article.pk)
    else:
        context = {
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comments = Comment()
        comments.article_id = article_pk
        comments.content = content
        # embed()
        comments.save()
        # embed()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)
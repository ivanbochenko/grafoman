from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST


def index(request):
    articles = Article.objects.order_by('uwords')
    context = {'articles': articles}
    return render(request, 'article/index.html', context)


def addArticle(request):

    form = ArticleForm()

    context = {'form': form}

    return render(request, 'article/addArticle.html', context)


@require_POST
def add(request):
    form = ArticleForm(request.POST)

    count_text = request.POST['text']
    num = len(set(count_text.split()))

    if form.is_valid():
        new_article = Article(title=request.POST['title'], text=request.POST['text'], uwords=num)
        new_article.save()

    return redirect('addArticle')

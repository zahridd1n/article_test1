from django.shortcuts import render, redirect
from unicodedata import category

from . import models


def home(request):
    articles = models.Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "index.html", context)






def article_detail(request, article_id):
    article = models.Article.objects.get(id=article_id)
    categorys = models.Category.objects.all()[:5]
    top_article = models.Article.objects.filter(category=article.category)[:5]
    data = list(top_article)
    for i in data:
        if i.id == article_id:
            data.remove(i)

    context = {
        "article": article,
        "categorys": categorys,
        "top_article": data,
    }

    return render(request, "detail_page.html", context)


def filter_article(request, category_id):
    articles = models.Article.objects.filter(category_id=category_id)

    context = {
        "articles": articles,
    }

    return render(request, "filter_article.html", context)
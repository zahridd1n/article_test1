from django.shortcuts import render, redirect
from unicodedata import category

from . import models


def home(request):
    articles = models.Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "index.html", context)

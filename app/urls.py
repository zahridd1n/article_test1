from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("detail-page/<int:article_id>/",views.article_detail, name="article_detail"),
    path("filter-article/<int:category_id>/",views.filter_article, name="filter_article"),
]
from django.urls import path
from django_blog.blog.django_blog.views import Home, Article

urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]

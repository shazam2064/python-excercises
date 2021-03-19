from django.test import TestCase
from blog.models import ArticleModel
from datetime import datetime
from django.utils import timezone


# Create your tests here.
class ArticleTest(TestCase):
    def test_article_created_success(self):
        ArticleModel.objects.create(title="test article", category="test category", author="test author",
                                    content="test content", created_at=datetime.now(tz=timezone.utc))
        article = ArticleModel.objects.get(title="test article")
        self.assertEqual(article.category, "test category2")


class BlogPagesTest(TestCase):
    def test_home_page_content(self):
        res = self.client.get("/blog/")
        self.assertEqual(res.content, b"Welcome to my blog!")

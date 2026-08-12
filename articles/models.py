from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):

    CATEGORY_CHOICES = [
        ("Politics", "Politics"),
        ("Sports", "Sports"),
        ("Technology", "Technology"),
        ("Business", "Business"),
        ("Entertainment", "Entertainment"),
        ("World", "World"),
        ("Health", "Health"),
    ]

    title = models.CharField(max_length=200)

    body = models.TextField()

    image = models.ImageField(
        upload_to="articles/",
        blank=True,
        null=True,
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_articles",
        blank=True,
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="World",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("home")



class Comment(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.author} - {self.article.title}"
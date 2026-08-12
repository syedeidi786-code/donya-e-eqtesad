from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article, Comment


def is_author(user):
    return user.groups.filter(name="Authors").exists()


# =========================
# HOME
# =========================

def home(request):

    query = request.GET.get("q", "")

    articles = Article.objects.all().order_by("-created_at")

    if query:
        articles = articles.filter(
            title__icontains=query
        )

    return render(
        request,
        "articles/home.html",
        {
            "articles": articles,
            "query": query,
        },
    )


# =========================
# ARTICLE DETAIL
# =========================

def article_detail(request, id):

    article = get_object_or_404(
        Article,
        id=id,
    )

    liked = False

    if request.user.is_authenticated:

        liked = article.likes.filter(
            id=request.user.id
        ).exists()

    return render(
        request,
        "articles/article_detail.html",
        {
            "article": article,
            "liked": liked,
        },
    )


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    articles = Article.objects.filter(
        author=request.user
    ).order_by("-created_at")

    return render(
        request,
        "articles/dashboard.html",
        {
            "articles": articles,
        },
    )


# =========================
# CREATE ARTICLE
# =========================

@login_required
def article_create(request):

    if request.method == "POST":

        form = ArticleForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            article = form.save(
                commit=False
            )

            article.author = request.user

            article.save()

            return redirect("dashboard")

    else:

        form = ArticleForm()

    return render(
        request,
        "articles/article_create.html",
        {
            "form": form,
        },
    )


# =========================
# UPDATE ARTICLE
# =========================

@login_required
def article_update(request, id):

    article = get_object_or_404(
        Article,
        id=id,
        author=request.user,
    )

    if request.method == "POST":

        form = ArticleForm(
            request.POST,
            request.FILES,
            instance=article,
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    else:

        form = ArticleForm(
            instance=article
        )

    return render(
        request,
        "articles/article_update.html",
        {
            "form": form,
        },
    )


# =========================
# DELETE ARTICLE
# =========================

@login_required
def article_delete(request, id):

    article = get_object_or_404(
        Article,
        id=id,
        author=request.user,
    )

    if request.method == "POST":

        article.delete()

        return redirect("dashboard")

    return render(
        request,
        "articles/article_delete.html",
        {
            "article": article,
        },
    )


# =========================
# LIKE ARTICLE
# =========================

@login_required
def like_article(request, id):

    article = get_object_or_404(
        Article,
        id=id
    )

    if request.method == "POST":

        if request.user in article.likes.all():

            article.likes.remove(
                request.user
            )

        else:

            article.likes.add(
                request.user
            )

    return redirect(
        "article_detail",
        id=id
    )


# =========================
# ADD COMMENT
# =========================

@login_required
def add_comment(request, id):

    article = get_object_or_404(
        Article,
        id=id
    )

    if request.method == "POST":

        comment_text = request.POST.get(
            "body"
        )

        if comment_text:

            Comment.objects.create(
                article=article,
                author=request.user,
                body=comment_text
            )

    return redirect(
        "article_detail",
        id=id
    )
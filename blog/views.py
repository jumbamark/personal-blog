from django.shortcuts import render
from .models import Post, Category

# Create your views here.


def homePage(request):
    # loading 10 posts from the database
    posts = Post.objects.all()[:11]
    categories = Category.objects.all()
    # print(posts)
    context = {
        "Posts": posts,
        "Categories": categories,
    }
    return render(request, "home.html", context)


def postsPage(request, url):
    blog = Post.objects.get(url=url)
    categories = Category.objects.all()
    context = {
        "Blog": blog,
        "Categories": categories,
    }
    return render(request, "posts.html", context)


def categoriesPage(request, url):
    category = Category.objects.get(url=url)
    posts = Post.objects.filter(category=category)
    context = {
        "Category": category,
        "Posts": posts,
    }
    return render(request, "categories.html", context)


def aboutPage(request):
    return render(request, "about.html")


def error_404(request, exception):
    return render(request, "404.html")

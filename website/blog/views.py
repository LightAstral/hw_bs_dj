import random

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q
from .forms import PostForm


# Create your views here.
def dummy():
    return str(random.randint(1, 10))


def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count // 2 + 1
    return {"cat1": all[:half], "cat2": all[half:]}


def index(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(title__contains='python')
    # posts = Post.objects.filter(published_date__year=2023)
    # posts = Post.objects.filter(category__name___iexact='python')
    posts = Post.objects.order_by('-published_date')
    # categories = Category.objects.all()

    context = {'posts': posts}
    context.update(get_categories())

    return render(request, "blog/index.html", context=context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    context = {"post": post}
    context.update(get_categories())

    return render(request, "blog/post.html", context=context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())

    return render(request, "blog/index.html", context=context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def services(request):
    return render(request, "blog/services.html")


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())

    return render(request, "blog/index.html", context=context)


def create(request):
    form = PostForm()
    context = {'form': form}
    return render(request, "blog/create.html", context=context)

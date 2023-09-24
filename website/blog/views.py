import random

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .models import Post, Category, Comment
from django.db.models import Q
from .forms import PostForm, CommentForm


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

    return render(request, 'blog/index.html', context=context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    context = {"post": post, "comments": comments, 'comment_form': comment_form}
    context.update(get_categories())

    return render(request, 'blog/post.html', context=context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())

    return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def services(request):
    return render(request, 'blog/services.html')


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())

    return render(request, 'blog/index.html', context=context)


def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.save()
            return index(request)
    context = {'form': form}
    return render(request, 'blog/create.html', context=context)


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Устанавливаем связь с постом
            comment.author = request.user if request.user.is_authenticated else None
            comment.save()
            return render(request, "blog/post.html", context={'post': post, 'comments': post.comments.all()})

    # В случае GET запроса или если форма не прошла валидацию, нужно вернуть форму и комментарии
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    context = {"post": post, "comments": comments, 'comment_form': comment_form}
    context.update(get_categories())
    return render(request, "blog/post.html", context=context)

# def add_comment(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         if text:
#             comment = Comment.objects.create(author=request.user if request.user.is_authenticated else None, text=text)
#             post.comments.add(comment)  # Добавляем комментарий к посту
#             comments = Comment.objects.filter(post_comments=post)  # Получаем комментарии для данного поста
#             context = {"post": post, "comments": comments}
#             context.update(get_categories())
#             return render(request, "blog/post.html", context=context)
#
#     comments = Comment.objects.filter(post_comments=post)  # Получаем комментарии для данного поста
#     context = {"post": post, "comments": comments}
#     context.update(get_categories())
#     return render(request, "blog/post.html", context=context)


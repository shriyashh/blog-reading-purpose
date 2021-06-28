from django.shortcuts import render
from blogapp.models import Post, Comment
from .forms import CommentForm


def blogindex(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        "posts": posts,
    }
    return render(request, "blogapp/blogindex.html", context)



def blogcategory(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blogapp/blogcategory.html", context)    


def blogdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blogapp/blogdetails.html", context)
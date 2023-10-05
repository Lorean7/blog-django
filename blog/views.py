from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id_post):
    post = get_object_or_404(Post, id=id_post, status=Post.Status.PUBLISHED)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):
    model = Post
    #template_name = 'blog/post_list.html'

# Create your views here.
# FBV
# def index(request):
#     posts = Post.objects.all().order_by('-pk')  # 최신순으로 정렬
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#
#     )
#


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }

    )

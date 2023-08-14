from django.shortcuts import render
from django.http import Http404
from .source import posts


def index(request):
    template = 'blog/index.html'
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    try:
        template = 'blog/detail.html'
        context = {
            'post': posts[id]
        }
        return render(request, template, context)
    except KeyError:
        raise Http404("Post does not exist")


def category_posts(request, category_slug):
    context = {
        'category_slug': category_slug
    }
    return render(request, 'blog/category.html', context)

# from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


# def index(request):
#     return redirect('app/')
#
# def file_view(request):
#     return render(request, template_name='news.html')

class NewsList(ListView):
    model = Post
    # ordering = '-dateCreation'
    queryset = Post.objects.order_by(
        '-dateCreation'
    )
    template_name = 'flatpages/news.html'
    context_object_name = 'PostCategory'


class NewDetail(DetailView):
    model = Post
     # ordering = '-dateCreation'
    # queryset = Post.objects.order_by(
    #     '-dateCreation'
    # )
    template_name = 'flatpages/new.html'
    context_object_name = 'PostCategory'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['time_now'] = datetime.utcnow()
    #     # context['next_news'] = None
    #     context['tag'] = Post.categoryType.values('categoryType')
    #     return context


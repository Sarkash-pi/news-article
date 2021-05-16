from django.shortcuts import render
from django.views import generic

from .models import Article


# Create your views here.
class ArticleListView(generic.ListView):
    model = Article


class ArticleDetailView(generic.DetailView):
    pass


class ArticleCreateView(generic.CreateView):
    pass


class ArticleUpdateView(generic.UpdateView):
    pass


class ArticleDeleteView(generic.DeleteView):
    pass

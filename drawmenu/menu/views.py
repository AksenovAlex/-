from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category


class CategoryListView(ListView):
    model = Category
    template_name = "menu/category_list.html"


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'menu/post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['name'] = self.category
        return context

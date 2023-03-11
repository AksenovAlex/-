from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
    ]
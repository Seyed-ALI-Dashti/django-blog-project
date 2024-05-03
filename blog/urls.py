from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts_page'),
    path('posts/<slug:slug>', views.single_post, name='post_detail_page'),
]
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='home'),
    path('create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
]
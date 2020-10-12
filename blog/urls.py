from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='home'),
    path('create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreateView.as_view(), name='blog-comment'),
]

urlpatterns += [ 
    # <pk> is identification for id field, 
    # slug can also be used 
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='blog-delete'), 
    path('comment/<int:pk>/delete/', views.BlogCommentDeleteView.as_view(), name='blog-comment-delete'), 
]
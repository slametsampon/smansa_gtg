# accounts/urls.py
from django.urls import path
from .views import SmansaUserCreateView, BloggerListView, BloggerDetailView
# Use include() to add paths from the catalog application 
from django.urls import include

app_name = 'accounts'
urlpatterns = [
    path('signup/', SmansaUserCreateView.as_view(), name='signup'),
    path('bloggers/', BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', BloggerDetailView.as_view(), name='blogger-detail'),
]

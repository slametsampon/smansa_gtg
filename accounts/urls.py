# accounts/urls.py
from django.urls import path
from . import views 
#import SmansaUserCreateView, BloggerListView, BloggerDetailView, SmansaUserVerifyView
# Use include() to add paths from the catalog application 
from django.urls import include

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SmansaUserCreateView.as_view(), name='signup'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('verify/<int:pk>/', views.SmansaUserVerifyView.as_view(), name='smnasa_user-verify'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]

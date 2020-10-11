# accounts/urls.py
from django.urls import path
from . import views 
from django.urls import include

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SmansaUserCreateView.as_view(), name='signup'),
    path('admin/', views.AdminSmansaView.as_view(), name='admin'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('new_comers/', views.BloggerNewListView.as_view(), name='bloggers-new'),
    path('active/', views.BloggerActiveListView.as_view(), name='bloggers-active'),
    path('verify/<int:pk>/', views.SmansaUserVerifyView.as_view(), name='smnasa_user-verify'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(),name='home'),  
    path('post/teste/', views.hello, name='hello'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.BlogDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
   

]
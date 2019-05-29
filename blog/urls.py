from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(),name='home'),
]
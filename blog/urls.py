from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # here the name is given model_form because it is shared between update view also
    path('about/', views.about, name='blog-about'),
]
"""
pk helps to drag the variable from url and use it.detailView grabs the variable pk and use implicitly
it passes the variable to the class based view, detailView expects the pk variable, we can change it by adding attribute to the class
"""


from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Post_list.as_view(), name='post_list'),
    path('post/<int:pk>', views.Post_detail.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update_post'),
    path('drafts/', views.DraftListView.as_view(), name='drafts'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='post_comment'),
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove')

]

from django.urls import path
from theblog.views import Postview,Detailview,AddPost,UpdatePost,DeletePost
urlpatterns = [
    path("post/", Postview.as_view(),name="post"),
    path('article/<int:pk>', Detailview.as_view(), name="article"),
    path('add_post/', AddPost.as_view(), name='add_blog'),
    path("update_post/edit/<int:pk>",UpdatePost.as_view(), name="update_post"),
    path("new_page/<int:pk>", DeletePost.as_view(), name="delete_post"),
]

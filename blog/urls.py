from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #path('', views.index),
    #path('<int:pk>/', views.single_post_page),
]

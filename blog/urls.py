from django.urls import path
from .views import *
urlpatterns=[
    # path('',index,name="home"),
    path('',Home.as_view,name="home"),
    # path('category/<int:slug>/',get_category,name="category"),
    path('category/<str:slug>/',PostByCategory.as_view(),name="category"),
path('tag/<str:slug>/',PostByTag.as_view(),name="tag"),
    path('post/<str:slug>/',GetPost.as_view,name="post"),
    path('search/<',Search.as_view,name="search"),
    path('test/',test,name='test'),
    path('test/rubric/<int:pk>',get_rubric,name='rubric'),
    # path('post/<str:slug>/',get_post,name="post"),
]

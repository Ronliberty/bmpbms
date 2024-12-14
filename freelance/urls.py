from django.urls import path
from .views import (
    ManagerPostListView, PostDetailView, PostCreateView, PostDeleteView,
    ManagerNewsListView, NewsDetailView, NewsCreateView, NewsDeleteView,
    DefaultNewsListView, DefaultPostListView, DefaultToolsListView,
     ToolCreateView, SkillCreateView, ManagerToolsListView, SkillsDeleteView, ToolsDeleteView,
    ManagerSkillsListView, DefaultSkillsListView, SkillsDetailView, ToolsDetailView
)

app_name = 'freelance'

urlpatterns = [
    path('post/manager/', ManagerPostListView.as_view(), name='manager_post_list'),
    path('post/default/', DefaultPostListView.as_view(), name='default_post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('news/manager/', ManagerNewsListView.as_view(), name='manager_news_list'),
    path('news/default/', DefaultNewsListView.as_view(), name='default_news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('tools/default/', DefaultToolsListView.as_view(), name='default_tools_list'),
    path('tools/create/', ToolCreateView.as_view(), name='tool_create'),
    path('tools/manager/', ManagerToolsListView.as_view(), name='manager_tools_list'),
    path('tools/<int:pk>/', ToolsDetailView.as_view(), name='tool_detail'),
    path('tools/delete/<int:pk>/', ToolsDeleteView.as_view(), name='tools_delete'),
    path('skills/default/', DefaultSkillsListView.as_view(), name='default_skills_list'),
    path('skills/manager/', ManagerSkillsListView.as_view(), name='manager_skills_list'),
    path('skills/create/', SkillCreateView.as_view(), name='skill_create'),
    path('skills/delete/<int:pk>/', SkillsDeleteView.as_view(), name='skills_delete'),
    path('skills/<int:pk>/', SkillsDetailView.as_view(), name='skill_detail'),
]

from django.urls import path
from .views import AgentCreateView, AgentListView
from .views import user_list_view

app_name = 'agent'
urlpatterns = [
    path('agent/create/', AgentCreateView.as_view(), name='agent-create'),
    path('agent/list/', AgentListView.as_view(), name='agent-list'),
    path('users/', user_list_view, name='user_list'),
]
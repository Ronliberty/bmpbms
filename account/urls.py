from django.urls import path
from .import views
from .views import role_based_redirect


app_name = 'account'
urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('account/', views.accountSettings, name='account'),
    path('role-based-redirect/', role_based_redirect, name='role_based_redirect'),
    path('profile/', views.display, name='display'),
    path('notification', views.notifications, name='notify'),
    path('search', views.search, name='search'),
    path('help/', views.help, name='help'),
    path('policies', views.policies, name='policy'),
    path('manager/policies/', views.manager_policies, name='manager-policy'),
    path('manager/help/', views.manager_help, name='manager-help'),
    path('tutorial/', views.tutorial, name='tutorial-default'),
    path('manager/tutorial/', views.create_tutorial, name='manager-tutorial'),
    path('tutorial/list/', views.list_tutorial, name='tutorial-list')

 ]
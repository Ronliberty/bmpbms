from django.urls import path
from .views import ServiceCreateView, ServiceListView, DefaultListView, ServiceRequestCreateView, ServiceRequestSuccessView, ManagerRequestView, HistoryServiceView, ServiceRequestStatusUpdateView


app_name = 'services'
urlpatterns = [
    path('service/create/', ServiceCreateView.as_view(), name='service-create'),
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('default/list', DefaultListView.as_view(), name='default-list'),
    path('request-service/', ServiceRequestCreateView.as_view(), name='request-service'),
    path('service-request-success/', ServiceRequestSuccessView.as_view(), name='service-request-success'),
    path('manger/request', ManagerRequestView.as_view(), name='manager-request'),
    path('history/service', HistoryServiceView.as_view(), name='history-service'),
    path('manager/request/<int:pk>/update/', ServiceRequestStatusUpdateView.as_view(), name='service-request-update'),
]
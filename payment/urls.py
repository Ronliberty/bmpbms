from django.urls import path
from .views import (
    InvoiceCreateView,
    ManagerInvoiceListView,
    DefaultInvoiceListView,
    InvoiceUpdateView,
    InvoiceDeleteView, AnalyticsCreateView, ManagerAnalyticsListView, AnalyticsDeleteView, AnalyticsDetailView, AnalyticsUpdateView, DefaultAnalyticsListView
)
app_name = 'payment'
urlpatterns = [
    path('invoices/create/', InvoiceCreateView.as_view(), name='create_invoice'),
    path('invoices/manager/', ManagerInvoiceListView.as_view(), name='manager_invoice_list'),
    path('invoices/default/', DefaultInvoiceListView.as_view(), name='default_invoice_list'),
    path('invoices/edit/<int:pk>/', InvoiceUpdateView.as_view(), name='edit_invoice'),
    path('invoices/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='delete_invoice'),
    path('analytics/edit/<int:pk>/', AnalyticsUpdateView.as_view(), name='edit_analytics'),
    path("analytics/<int:pk>/", AnalyticsDetailView.as_view(), name="analytics-detail"),
    path('analytic/create/', AnalyticsCreateView.as_view(), name='analytics-create'),
    path('analytics/manager/', ManagerAnalyticsListView.as_view(), name='manager_analytics_list'),
    path('analytics/default/', DefaultAnalyticsListView.as_view(), name='default_analytics_list'),
    path('analytics/delete/<int:pk>/', AnalyticsDeleteView.as_view(), name='delete_analytics'),
]

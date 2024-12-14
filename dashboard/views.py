from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView


class BaseDashboardView(LoginRequiredMixin, TemplateView):
    group_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name=self.group_name).exists():
            messages.error(request, "You are not authorized to access this page.")
            return redirect('base:index')
        return super().dispatch(request, *args, **kwargs)

class ClientDashboardView(BaseDashboardView):
    template_name = 'dashboard/client_dashboard.html'
    group_name = 'default'

class ManagerDashboardView(BaseDashboardView):
    template_name = 'dashboard/manager_dashboard.html'
    group_name = 'manager'




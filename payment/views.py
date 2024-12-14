from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Invoice, Analytics
from .forms import InvoiceForm, AnalyticsForm



# Create Invoice (for Managers only)
class InvoiceCreateView(UserPassesTestMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'payment/invoice_form.html'
    success_url = reverse_lazy('payment:manager_invoice_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Ensure this line is present
        return super().form_valid(form)



# List Invoices for Managers
class ManagerInvoiceListView(UserPassesTestMixin, ListView):
    model = Invoice
    template_name = 'payment/manager_invoice_list.html'
    context_object_name = 'invoices'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Invoice.objects.filter(created_by=self.request.user)


# List Invoices for Default Users
class DefaultInvoiceListView(UserPassesTestMixin, ListView):
    model = Invoice
    template_name = 'payment/default_invoice_list.html'
    context_object_name = 'invoices'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Invoice.objects.filter(recipient_user=self.request.user)


# Edit Invoice (for Managers only)
class InvoiceUpdateView(UserPassesTestMixin, UpdateView):
    model = Invoice
    fields = ['description', 'amount_to_pay', 'recipient_user']  # Correct field names
    template_name = 'payment/invoice_form.html'
    success_url = reverse_lazy('payment:manager_invoice_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Invoice.objects.filter(created_by=self.request.user)



# Delete Invoice (for Managers only)
class InvoiceDeleteView(UserPassesTestMixin, DeleteView):
    model = Invoice
    template_name = 'payment/invoice_confirm_delete.html'
    success_url = reverse_lazy('payment:manager_invoice_list')
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()





class AnalyticsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Analytics
    form_class = AnalyticsForm
    template_name = "payment/analytics_form.html"
    success_url = reverse_lazy('payment:manager_analytics_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.manager = self.request.user  # Ensure this line is present
        return super().form_valid(form)


class ManagerAnalyticsListView(UserPassesTestMixin, ListView):
    model = Analytics
    template_name = 'payment/manager_analytic_list.html'
    context_object_name = 'analytics'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Analytics.objects.filter(manager=self.request.user)

class DefaultAnalyticsListView(UserPassesTestMixin, ListView):
    model = Analytics
    template_name = 'payment/default_analytics_list.html'
    context_object_name = 'analytics'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Analytics.objects.filter(target_user=self.request.user)


class AnalyticsUpdateView(UserPassesTestMixin, UpdateView):
    model = Analytics
    fields = ['image', 'description', 'amount', 'target_user']  # Correct field names
    template_name = 'payment/analytics_form.html'
    success_url = reverse_lazy('payment:manager_analytics_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Analytics.objects.filter(manager=self.request.user)


class AnalyticsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Analytics
    template_name = "payment/analytics_confirm_delete.html"
    success_url = reverse_lazy('payment:manager_analytics_list')
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()










class AnalyticsDetailView(LoginRequiredMixin, DetailView):
    model = Analytics
    template_name = "payment/analytics_detail.html"
    context_object_name = 'analytic'

    def get_object(self):
        # Fetch the Analytics object based on the 'id' passed in the URL
        return Analytics.objects.get(id=self.kwargs['pk'])
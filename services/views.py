from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, ServiceImage, ServiceRequest
from .forms import ServiceForm, ServiceImageForm, ServiceRequestForm, ServiceRequestStatusForm
from django.http import JsonResponse
from django.template.loader import render_to_string

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('services:service-list')




    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_formset'] = modelformset_factory(ServiceImage, form=ServiceImageForm, extra=3)(self.request.POST, self.request.FILES, queryset=ServiceImage.objects.none())
        else:
            data['image_formset'] = modelformset_factory(ServiceImage, form=ServiceImageForm, extra=3)(queryset=ServiceImage.objects.none())
        return data

    def form_valid(self, form):
        # Set the created_by user to the currently logged-in user
        form.instance.created_by = self.request.user
        self.object = form.save()

        # Save images from the formset
        image_formset = modelformset_factory(ServiceImage, form=ServiceImageForm, extra=3)(self.request.POST, self.request.FILES)
        if image_formset.is_valid():
            for image_form in image_formset:
                if image_form.cleaned_data:
                    image_instance = image_form.save(commit=False)
                    image_instance.service = self.object
                    image_instance.save()

        return redirect(self.success_url)

class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get(self, request, *args, **kwargs):
        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Render the service list partial template and return it as a JSON response
            services_html = render_to_string(self.template_name, {'services': self.get_queryset()}, request=request)
            return JsonResponse({'html': services_html})
        else:
            # For normal requests, render the full page
            return super().get(request, *args, **kwargs)

class DefaultListView(UserPassesTestMixin, ListView):
    model = Service
    template_name = 'services/default_list.html'
    context_object_name = 'services'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Service.objects.all

class ServiceRequestCreateView(UserPassesTestMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'services/request_service.html'
    success_url = reverse_lazy('services:service-request-success')

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def form_valid(self, form):
        # Set the requested_by field to the logged-in user
        form.instance.requested_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        # Simply render the form with errors on failure
        return super().form_invalid(form)


class ServiceRequestSuccessView(TemplateView):
    template_name = 'services/service_request_success.html'  # Template to render for success page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Your service request has been successfully submitted!'
        return context

class HistoryServiceView(UserPassesTestMixin, ListView):
    model = ServiceRequest
    template_name = 'services/history_service.html'
    context_object_name = 'servicerequests'

    def get_queryset(self):
        # Filter the ServiceRequest objects by the logged-in user
        return ServiceRequest.objects.filter(requested_by=self.request.user)

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()


class ManagerRequestView(UserPassesTestMixin, ListView):
    model = ServiceRequest
    template_name = 'services/manager_list.html'
    context_object_name = 'servicerequests'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

class ServiceRequestStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ServiceRequest
    form_class = ServiceRequestStatusForm
    template_name = 'services/manager_update.html'

    def test_func(self):
        # Ensure only managers can access this view
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        # Optionally, you can add logic here (e.g., notify the user of status changes)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('services:manager-request')
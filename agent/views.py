from django.shortcuts import render, redirect
from .models import OurAgent, AgentImage
from .forms import AgentForm, AgentImageForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class AgentCreateView(LoginRequiredMixin, CreateView):
    model = OurAgent
    form_class = AgentForm
    template_name = 'agent/create.html'
    success_url = reverse_lazy ('agent:agent-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        ImageFormset = modelformset_factory(AgentImage, form=AgentImageForm, extra=3)
        if self.request.POST:
            data['image_formset'] = modelformset_factory(AgentImage, form=AgentImageForm, extra=3)(self.request.POST, self.request.FILES, queryset=AgentImage.objects.none())
        else:
            data['image_formset'] = modelformset_factory(AgentImage, form=AgentImageForm, extra=3)(queryset=AgentImage.objects.none())
            return data

    def form_valid(self, form):

        form.instance.created_by = self.request.user
        self.object = form.save()

        context = self.get_context_data()
        image_formset = context['image_formset']

        if image_formset.is_valid():
            for image_form in image_formset:
                if image_form.cleaned_data:
                    image_instance = image_form.save(commit=False)
                    image_instance.expert = self.object
                    image_instance.save()
        else:
            return self.form_invalid(form)

        return redirect(self.success_url)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class AgentListView(LoginRequiredMixin, ListView):
    model = OurAgent
    template_name = 'agent/expert_list.html'
    context_object_name = 'agent'


    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)

def user_list_view(request):
    users = User.objects.all().prefetch_related('groups')
    return render(request, 'agent/user_list.html', {'users': users})
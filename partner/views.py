from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import PartnershipArea, PartnershipQuestion, PartnershipChoice, PartnershipAnswer
from .forms import PartnerForm, QuestionForm,ChoiceForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import modelformset_factory
from django.shortcuts import render

class PartnershipCreateView(UserPassesTestMixin, CreateView):
    model = PartnershipArea
    form_class = PartnerForm
    template_name = 'partner/create_partner.html'
    success_url = reverse_lazy('partner:manager_partnership_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ManagerPartnershipListView(UserPassesTestMixin, ListView):
    model = PartnershipArea
    template_name = 'partner/partnership_list.html'
    context_object_name = 'partnership'
    required_role = 'manager'
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()
    def get_queryset(self):
        return PartnershipArea.objects.filter(created_by=self.request.user)

class DefaultPartnershipListView(UserPassesTestMixin, ListView):
    model = PartnershipArea
    template_name = 'partner/default_partnership_list.html'
    context_object_name = 'partnership'
    required_role = 'default'
    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return PartnershipArea.objects.all

class PartnershipQuestionCreateView(UserPassesTestMixin, CreateView):
    model = PartnershipQuestion
    form_class = QuestionForm
    template_name = 'partner/create_question.html'
    success_url = reverse_lazy('partner:manager_question_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ChoiceFormSet = modelformset_factory(PartnershipChoice, form=ChoiceForm, extra=3)  # 3 extra fields for choices
        context['choice_formset'] = ChoiceFormSet(queryset=PartnershipChoice.objects.none())
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()
    def form_valid(self, form):
        question = form.save(commit=False)
        question.created_by = self.request.user
        question.save()

        # Handle multiple-choice options
        ChoiceFormSet = modelformset_factory(PartnershipChoice, form=ChoiceForm, extra=0)
        formset = ChoiceFormSet(self.request.POST)

        if question.is_multiple_choice and formset.is_valid():
            for choice_form in formset:
                choice = choice_form.save(commit=False)
                choice.question = question
                choice.save()

        return super().form_valid(form)

class ManagerQuestionListView(UserPassesTestMixin, ListView):
    model = PartnershipQuestion
    template_name = 'partner/question_list.html'
    context_object_name = 'question'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return PartnershipQuestion.objects.filter(created_by=self.request.user)

class DefaultQuestionListView(UserPassesTestMixin, ListView):
    model = PartnershipQuestion
    template_name = 'partner/default_question.html'
    context_object_name = 'question'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        partnership_area_id = self.request.GET.get('partnership_area')
        if partnership_area_id:
            return PartnershipQuestion.objects.filter(partnership_area_id=partnership_area_id)
        return PartnershipQuestion.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partnership_area_id = self.request.GET.get('partnership_area')
        if partnership_area_id:
            context['partnershiparea'] = PartnershipArea.objects.get(id=partnership_area_id)
        return context

class PartnershipAnswerCreateView(UserPassesTestMixin, CreateView):
    model = PartnershipAnswer
    template_name = "partner/default_question.html"
    fields = ['selected_choice', 'answer_text']  # Both fields to accommodate multiple choice and open-ended

    def form_valid(self, form):
        question = PartnershipQuestion.objects.get(pk=self.kwargs['question_id'])
        form.instance.question = question
        form.instance.answered_by = self.request.user

        # Ensure logic for multiple-choice vs open-ended
        if question.is_multiple_choice and not form.instance.selected_choice:
            form.add_error('selected_choice', 'You must select a choice for this question.')
            return self.form_invalid(form)
        elif not question.is_multiple_choice and not form.instance.answer_text:
            form.add_error('answer_text', 'You must provide an answer for this question.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('partner:question_list', kwargs={'area_id': self.object.question.partnership_area.id})

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .models import Post, News, Tool, Skill
from .forms import PostForm, NewsForm, ToolForm, SkillForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def is_manager(user):
    return user.groups.filter(name='managers').exists()

# Post Views
class ManagerPostListView(UserPassesTestMixin, ListView):
    model = Post
    template_name = 'freelance/post_list.html'
    context_object_name = 'post'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

class DefaultPostListView(UserPassesTestMixin, ListView):
    model = Post
    template_name = 'freelance/default_Post_list.html'
    context_object_name = 'post'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Post.objects.all

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'freelance/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'freelance/post_form.html'
    success_url = reverse_lazy('freelance:manager_post_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Ensure this line is present
        return super().form_valid(form)

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'freelance/post_confirm_delete.html'
    success_url = reverse_lazy('freelance:manager_post_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

# News Views
class ManagerNewsListView(UserPassesTestMixin, ListView):
    model = News
    template_name = 'freelance/news_list.html'
    context_object_name = 'news_item'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return News.objects.filter(created_by=self.request.user)

class DefaultNewsListView(UserPassesTestMixin, ListView):
    model = News
    template_name = 'freelance/default_news_list.html'
    context_object_name = 'news_item'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return News.objects.all

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'freelance/news_detail.html'
    context_object_name = 'news_item'

class NewsCreateView( UserPassesTestMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'freelance/news_form.html'
    success_url = reverse_lazy('freelance:manager_news_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Ensure this line is present
        return super().form_valid(form)

class NewsDeleteView( UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'freelance/news_confirm_delete.html'
    success_url = reverse_lazy('freelance:manager_news_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

# Tool Views

class ManagerToolsListView(UserPassesTestMixin, ListView):
    model = Tool
    template_name = 'freelance/tool_list.html'
    context_object_name = 'tools'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Tool.objects.filter(created_by=self.request.user)

class DefaultToolsListView(UserPassesTestMixin, ListView):
    model = Tool
    template_name = 'freelance/default_tools_list.html'
    context_object_name = 'tools'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Tool.objects.all
class ToolCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Tool
    form_class = ToolForm
    template_name = 'freelance/tool_form.html'
    success_url = reverse_lazy('freelance:manager_tools_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Ensure this line is present
        return super().form_valid(form)
class ToolsDeleteView(UserPassesTestMixin, DeleteView):
    model = Tool
    template_name = "freelance/tool_confirm_delete.html"
    success_url = reverse_lazy('freelance:manager_tools_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()




class ToolsDetailView(LoginRequiredMixin, DetailView):
    model = Tool
    template_name = 'freelance/tool_detail.html'
    context_object_name = 'tool_item'

class ManagerSkillsListView(UserPassesTestMixin, ListView):
    model = Skill
    template_name = 'freelance/skill_list.html'
    context_object_name = 'skill'
    required_role = 'manager'

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get_queryset(self):
        return Skill.objects.filter(created_by=self.request.user)

class DefaultSkillsListView(UserPassesTestMixin, ListView):
    model = Skill
    template_name = 'freelance/default_skill_list.html'
    context_object_name = 'skill'
    required_role = 'default'

    def test_func(self):
        return self.request.user.groups.filter(name='default').exists()

    def get_queryset(self):
        return Skill.objects.all

    def render_to_response(self, context, **kwargs):
        # Check if the request is AJAX
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Render the skills list to HTML string
            html = render_to_string(self.template_name, context, request=self.request)
            # Return the HTML inside a JsonResponse
            return JsonResponse({'html': html})

        # If it's not an AJAX request, return the regular response
        return super().render_to_response(context, **kwargs)

class SkillCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'freelance/skill_form.html'
    success_url = reverse_lazy('freelance:manager_skills_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Ensure this line is present
        return super().form_valid(form)


class SkillsDeleteView(UserPassesTestMixin, DeleteView):
    model = Skill
    template_name = "freelance/skill_confirm_delete.html"
    success_url = reverse_lazy('freelance:manager_skills_list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()




class SkillsDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'freelance/skill_detail.html'
    context_object_name = 'skill'
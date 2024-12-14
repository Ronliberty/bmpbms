from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from .forms import UserProfileForm, VideoForm
from .models import UserProfile, Tutorial
from django.db.models import Q
from freelance.models import Tool, Skill, News, Post
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()
def role_based_redirect(request):
    if request.user.groups.filter(name='manager').exists():
        return redirect('dashboard:manager_dashboard')
    elif request.user.groups.filter(name='default').exists():
        return redirect('dashboard:client_dashboard')
    else:
        messages.error(request, "Sign up today!.")
        return redirect('account:sign_up')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:tutorial-default')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def tutorial(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'account/tutorial.html', {'tutorials': tutorials})

def create_tutorial(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accountutorial-list')
    else:
            form = VideoForm()

    return render(request, 'account/create_tutorial.html', {'form': form})

def list_tutorial(request):
    return render(request, 'account/tutorial_list.html')

def accountSettings(request):

    if not request.user.groups.filter(name__in=['default', 'manager']).exists():
        return redirect('dashboard:client_dashboard')

    profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(instance=profile)


    if created:
        if request.user.groups.filter(name='manager').exists():
            return redirect('dashboard:manager_dashboard')
        elif request.user.groups.filter(name='default').exists():
            return redirect('dashboard:client_dashboard')


    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated successfully!')
            return redirect('account:account')


    context = {'form': form}
    return render(request, 'account/account_settings.html', context)


def display(request):
    return render(request, 'account/profile.html')


def notifications(request):
    return render(request, 'account/notification.html')

def help(request):
     return render(request, 'account/help.html')


def policies(request):
    return render(request, 'account/policy.html')

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')

        # Search across both 'name' and 'description' fields
        tools_results = Tool.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        skills_results = Skill.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        news_results = News.objects.filter(
            Q(headline__icontains=searched) | Q(content__icontains=searched)
            # Adjust if News has 'title' instead of 'name'
        )
        post_results = Post.objects.filter(
            Q(title__icontains=searched) | Q(description__icontains=searched)
            # Adjust if Post has 'content' instead of 'description'
        )

        context = {
            'searched': searched,
            'tools_results': tools_results,
            'skills_results': skills_results,
            'news_results': news_results,
            'post_results': post_results,
        }
        return render(request, 'account/search.html', context)
    else:
        return render(request, 'account/search.html')


def manager_policies(request):
    return render(request, 'account/create_policy.html')

def manager_help(request):
    return render(request, 'account/create-help.html')




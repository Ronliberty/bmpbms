from django import forms
from .models import Post, News, Tool, Skill

# Form for Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'link']

# Form for News
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline', 'content']

# Form for Tool
class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'link']

# Form for Skill
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

from django import forms
from .models import PartnershipArea, PartnershipQuestion, PartnershipChoice


class PartnerForm(forms.ModelForm):
    class Meta:
        model = PartnershipArea
        fields = ['name', 'description']
class QuestionForm(forms.ModelForm):
    class Meta:
        model = PartnershipQuestion
        fields = ['partnership_area', 'question_text']  # Include partnership_area

    # Optional: Add custom widget or placeholder for the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['partnership_area'].widget.attrs.update({'class': 'form-control'})
        self.fields['question_text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your question here'})

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = PartnershipChoice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter choice text'}),
        }
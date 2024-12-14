from django import forms
from .models import Invoice, Analytics
from django.contrib.auth.models import User
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['amount_to_pay', 'description', 'wallet_email_or_account', 'recipient_user']

class AnalyticsForm(forms.ModelForm):
    target_user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Analytics
        fields = ['image', 'description', 'amount', 'target_user']

from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    wallet_email_or_account = models.CharField(max_length=100)
    recipient_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invoices")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_invoices', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Invoice {self.id} for {self.recipient_user.username}"


class Analytics(models.Model):
    image = models.ImageField(upload_to='analytics/')
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_analytics", default=1)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="analytics")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analytics {self.id} for {self.target_user.username} (Created by {self.manager.username})"

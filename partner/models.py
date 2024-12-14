from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class PartnershipArea(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_Partnership')

    def __str__(self):
        return self.name


class PartnershipQuestion(models.Model):
    partnership_area = models.ForeignKey(PartnershipArea, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    is_multiple_choice = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', default=1)

    def __str__(self):
        return f"Question for {self.partnership_area.name}: {self.question_text}"

class PartnershipChoice(models.Model):
    question = models.ForeignKey(
        PartnershipQuestion,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Choice for '{self.question.question_text}': {self.choice_text}"

class PartnershipRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partnership_requests')
    partnership_area = models.ForeignKey(PartnershipArea, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Requested by {self.user.username} for {self.partnership_area.name}({self.status})"

class PartnershipAnswer(models.Model):
    partnership_reqeust = models.ForeignKey(PartnershipRequest, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(PartnershipQuestion, on_delete=models.CASCADE, related_name="answers")
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers", default=1)
    answer_text = models.TextField()
    selected_choice = models.ForeignKey(
        PartnershipChoice,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="answers"
    )  # For multiple-choice questions
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f"Answer by {self.answered_by.username} to '{self.question.question_text}'"

class PartnershipEngagement(models.Model):
    partnership_reqeust = models.ForeignKey(PartnershipRequest, on_delete=models.CASCADE, related_name="engagements")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="engagements")
    start_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Engagement for{self.partnership_reqeust.user.username} with{self.manager.user.username}"




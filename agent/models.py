from django.db import models
from django.contrib.auth.models import User


class OurAgent(models.Model):
    names = models.CharField(max_length=255, blank=True, null=True)
    portfolio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.names or "No name provided"

class AgentImage(models.Model):
    expert = models.ForeignKey(OurAgent, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='agent_images/')

    def __str__(self):
        return f"Image for {self.expert.names}"



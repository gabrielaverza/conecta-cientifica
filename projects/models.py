from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    advisor = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    subscribers = models.ManyToManyField(User, related_name='subscribed_projects', default=None, blank=True)
    requires_approval = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class SubscriptionRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True, blank=True)

class SubscriptionHistory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.project.title} - {self.approved}'
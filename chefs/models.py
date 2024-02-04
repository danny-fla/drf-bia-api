from django.db import models
from django.contrib.auth.models import User


class Chef(models.Model):
    """
    Chef model, related to User
    """
    CHEF_TYPE_CHOICES = [
        ('professional', 'Professional Chef'),
        ('home_cook', 'Home Cooking Enthusiast'),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    cuisine_speciality = models.CharField(max_length=255)
    experience = models.IntegerField()
    location = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the objects by latest created first
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s Chef Details"
from django.db import models
from django.contrib.auth.models import User
from chefs.models import Chef


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    chef = models.ForeignKey(
        Chef, on_delete=models.CASCADE, related_name='reviews',
        blank=True, null=True
    )
    content = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}' review"

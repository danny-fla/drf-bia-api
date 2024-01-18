from django.db import models
from django.contrib.auth.models import User
from quicksnap.models import Quicksnap



class QuicksnapComment(models.Model):
    """
    RecipeComment model, related to User and Quicksnap
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quicksnap = models.ForeignKey(
        Quicksnap, related_name='QuicksnapComments', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
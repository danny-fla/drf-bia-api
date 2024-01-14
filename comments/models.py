from django.db import models
from django.contrib.auth.models import User
from recipe.models import Recipe
from quicksnap import Quicksnap


class Comment(models.Model):
    """
    Comment model, related to User, Recipe and Quicksnap
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quicksnap = models.ForeignKey(Quicksnap, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
from django.db import models
from django.contrib.auth.models import User
from recipe.models import Recipe


class RecipeComment(models.Model):
    """
    RecipeComment model, related to User and Recipe
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='RecipeComments', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

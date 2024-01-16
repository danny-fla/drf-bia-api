from django.db import models
from django.contrib.auth.models import User
from recipe.models import Recipe


class RecipeLike(models.Model):
    """
    Like model, related to 'owner'and 'recipe'.
    'owner' is a User instance, 'recipe' is a 'Recipe' instance.'unique_together' makes sure a user can't like the
    same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f'{self.owner} {self.recipe}'

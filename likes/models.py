from django.db import models
from django.contrib.auth.models import User
from recipe.models import Recipe
from quicksnap.models import Quicksnap


class Like(models.Model):
    """
    Like model, related to 'owner', 'recipe' and 'quicksnap'.
    'owner' is a User instance, 'recipe' is a 'Recipe' instance and 'quicksnap'
    is a Quicksnap instance.'unique_together' makes sure a user can't like the
    same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='likes', on_delete=models.CASCADE
    )
    quicksnap = models.ForeignKey(
        Quicksnap, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'recipe', 'quicksnap']

    def __str__(self):
        return f'{self.owner} {self.recipe} {self.quicksnap}'

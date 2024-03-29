from django.db import models
from django.contrib.auth.models import User

RECIPE_CATEGORIES = (
    ("Breakfast", "Breakfast"),
    ("Snack", "Snack"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
)


class Recipe(models.Model):
    """
    Recipe model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    duration = models.DurationField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ynchgw', blank=True
    )
    category = models.CharField(
        max_length=50, choices=RECIPE_CATEGORIES, default='Dinner'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

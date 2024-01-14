from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Quicksnap(models.Model):
    """
    Quicksnap model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ynchgw'
    )
    city = models.CharField(max_length=255, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

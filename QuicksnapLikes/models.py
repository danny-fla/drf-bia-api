from django.db import models
from django.contrib.auth.models import User
from quicksnap.models import Quicksnap


class QuicksnapLike(models.Model):
    """
    QuicksnapLike model, related to 'owner'and 'Quicksnap'.
    'owner' is a User instance, 'Quicksnap' is a 'Quicksnap' instance.'unique_together' makes sure a user can't like the
    same Quicksnap twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quicksnap = models.ForeignKey(
        Quicksnap, related_name='QuicksnapLikes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'quicksnap']

    def __str__(self):
        return f'{self.owner} {self.quicksnap}'

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
#User is going to be sender, it will be sending the signal, post_save is signal
#when a user is saved, this post_save signal is sent, and is received by receiver, then which is
# create_profile function which takes these arguments(post_save signal has these arguments)
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()



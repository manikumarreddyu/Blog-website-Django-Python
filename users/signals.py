from django.db.models.signals import post_save  #sends signal after successful object creation
from django.contrib.auth.models import User     #signal sender -- model
from django.dispatch import receiver            #signal receiver -- function
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


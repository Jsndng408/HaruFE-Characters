from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is saved, send signal 'post_save', who the receiver, create_profile, will invoke
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# kwargs -> Accept any additional keyword arguments
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
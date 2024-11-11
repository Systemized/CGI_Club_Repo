from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

## ChatGPT with some 'minor' help since im so ass, so idk how bad or good this function is
# @receiver(pre_save, sender=Profile)
# def delete_old_profile_pic(sender, instance, **kwargs):
#     if instance.pk:  # Check if instance is already saved (update, not create)
#         old_profile = Profile.objects.get(pk=instance.pk)
#         if old_profile.image != instance.image and old_profile.image.name != 'default.jpg':
#             old_profile.image.delete(save=False)  # Delete the old file, don't save immediately



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
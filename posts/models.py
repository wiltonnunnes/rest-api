from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings

class Post(models.Model):
	title = models.CharField(max_length=30)
	text = models.CharField(max_length=280)
	owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

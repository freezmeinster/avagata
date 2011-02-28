from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	
	alamat = models.TextField(max_length=255)
	user = models.OneToOneField(User)
	
	class Meta:
		verbose_name_plural = "Daftar Profile Pengguna"
		verbose_name = "Pengguna"

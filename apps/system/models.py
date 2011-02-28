from django.db import models
from django.contrib.auth.models import User

class Provinsi(models.Model):
	nama_provinsi = models.CharField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'Daftar Nama Provinsi'
		
	def __unicode__(self):
		return self.nama_provinsi
	
		
class UserProfile(models.Model):
	
	provinsi = models.ForeignKey(Provinsi)
	alamat = models.TextField(max_length=255)
	user = models.OneToOneField(User)
	
	class Meta:
		verbose_name_plural = "Daftar Profile Pengguna"
		verbose_name = "Pengguna"

	def __unicode__(self):
		return self.alamat

from django.db import models
from django.contrib.auth.models import User
	
		
class UserProfile(models.Model):
	KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan'),
	)
	nama_lengkap = models.CharField(max_length=255)
	tgl_lahir = models.DateField()
	tgl_daftar = models.DateField()
	tempat_lahir = models.CharField(max_length=255)
	alamat = models.TextField(max_length=255)
	kelamin = models.CharField(max_length=1, choices=KELAMIN)
	user = models.OneToOneField(User)
	
	class Meta:
		verbose_name_plural = "Daftar Profile Pengguna"

	def __unicode__(self):
		return self.nama_lengkap

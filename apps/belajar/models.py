from django.db import models
from system.models import UserProfile
from django.contrib.auth.models import User

class MataPelajaran(models.Model):
	nama = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Mata Pelajaran'

	def __unicode__(self):
		return self.nama

class MateriPelajaran(models.Model):
	matapelajaran = models.ForeignKey(MataPelajaran)
	judul = models.CharField(max_length=255)
	isi = models.TextField()
	tgl_post = models.DateField()
	penulis = models.ForeignKey(UserProfile)
	
	class Meta:
		verbose_name_plural = 'Materi Pelajaran'
	
	def __unicode__(self):
		return self.judul

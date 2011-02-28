from django.db import models
from system.models import UserProfile
from django.contrib.auth.models import User

class MataPelajaran(models.Model):
	nama = models.CharField(max_length=50)

class MateriPelajaran(models.Model):
	matapelajaran = models.ForeignKey(MataPelajaran)
	judul = models.CharField(max_length=255)
	kontent = models.TextField()
	tgl_post = models.DateField()
	penulis = models.OneToOneField(UserProfile)

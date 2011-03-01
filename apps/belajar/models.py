from django.db import models
from system.models import UserProfile
from django.contrib.auth.models import User

class MataPelajaran(models.Model):
	nama = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Daftar Mata Pelajaran'

	def __unicode__(self):
		return self.nama

class MateriPelajaran(models.Model):
	matapelajaran = models.ForeignKey(MataPelajaran)
	judul = models.CharField(max_length=255)
	isi = models.TextField()
	tgl_post = models.DateField()
	penulis = models.ForeignKey(UserProfile)
	
	class Meta:
		verbose_name_plural = 'Daftar Materi Pelajaran'
	
	def __unicode__(self):
		return self.judul

class MateriSoal(models.Model):
	judul_soal = models.CharField(max_length=255)
	materi_pelajaran = models.ForeignKey(MateriPelajaran)
      	tgl_buat = models.DateField()
 
	class Meta:
		verbose_name_plural = "Daftar Soal Latihan"

	def __unicode__(self):
		return self.judul_soal

class PertanyaanSoal(models.Model):
	soal = models.TextField()
	jawaban = models.CharField(max_length=255)
	materi_soal = models.ManyToManyField(MateriSoal)
	
	class Meta:
		verbose_name_plural = "Daftar Pertanyaan"

	def __unicode__(self):
		return self.soal

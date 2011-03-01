from django.contrib import admin
from belajar.models import MataPelajaran, MateriPelajaran, MateriSoal,PertanyaanSoal

class MateriPelajaranAdmin(admin.ModelAdmin):
	search_fields = ("judul","isi")
	date_hierarchy = 'tgl_post'

class PertanyaanAdmin(admin.ModelAdmin):
	search_fields = ["soal"]

admin.site.register(MataPelajaran)
admin.site.register(MateriPelajaran, MateriPelajaranAdmin)
admin.site.register(MateriSoal)
admin.site.register(PertanyaanSoal, PertanyaanAdmin)

from django.contrib import admin
from belajar.models import MataPelajaran, MateriPelajaran

class MateriPelajaranAdmin(admin.ModelAdmin):
	search_fields = ("judul","konten")
	date_hierarchy = 'tgl_post'

admin.site.register(MataPelajaran)
admin.site.register(MateriPelajaran, MateriPelajaranAdmin)

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MataPelajaran'
        db.create_table('belajar_matapelajaran', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('belajar', ['MataPelajaran'])

        # Adding model 'MateriPelajaran'
        db.create_table('belajar_materipelajaran', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('matapelajaran', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['belajar.MataPelajaran'])),
            ('judul', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('isi', self.gf('django.db.models.fields.TextField')()),
            ('tgl_post', self.gf('django.db.models.fields.DateField')()),
            ('penulis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.UserProfile'])),
        ))
        db.send_create_signal('belajar', ['MateriPelajaran'])

        # Adding model 'MateriSoal'
        db.create_table('belajar_materisoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('judul_soal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('materi_pelajaran', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['belajar.MateriPelajaran'])),
            ('tgl_buat', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('belajar', ['MateriSoal'])

        # Adding model 'PertanyaanSoal'
        db.create_table('belajar_pertanyaansoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('soal', self.gf('django.db.models.fields.TextField')()),
            ('jawaban', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('belajar', ['PertanyaanSoal'])

        # Adding M2M table for field materi_soal on 'PertanyaanSoal'
        db.create_table('belajar_pertanyaansoal_materi_soal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pertanyaansoal', models.ForeignKey(orm['belajar.pertanyaansoal'], null=False)),
            ('materisoal', models.ForeignKey(orm['belajar.materisoal'], null=False))
        ))
        db.create_unique('belajar_pertanyaansoal_materi_soal', ['pertanyaansoal_id', 'materisoal_id'])


    def backwards(self, orm):
        
        # Deleting model 'MataPelajaran'
        db.delete_table('belajar_matapelajaran')

        # Deleting model 'MateriPelajaran'
        db.delete_table('belajar_materipelajaran')

        # Deleting model 'MateriSoal'
        db.delete_table('belajar_materisoal')

        # Deleting model 'PertanyaanSoal'
        db.delete_table('belajar_pertanyaansoal')

        # Removing M2M table for field materi_soal on 'PertanyaanSoal'
        db.delete_table('belajar_pertanyaansoal_materi_soal')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'belajar.matapelajaran': {
            'Meta': {'object_name': 'MataPelajaran'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'belajar.materipelajaran': {
            'Meta': {'object_name': 'MateriPelajaran'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isi': ('django.db.models.fields.TextField', [], {}),
            'judul': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'matapelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['belajar.MataPelajaran']"}),
            'penulis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.UserProfile']"}),
            'tgl_post': ('django.db.models.fields.DateField', [], {})
        },
        'belajar.materisoal': {
            'Meta': {'object_name': 'MateriSoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judul_soal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'materi_pelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['belajar.MateriPelajaran']"}),
            'tgl_buat': ('django.db.models.fields.DateField', [], {})
        },
        'belajar.pertanyaansoal': {
            'Meta': {'object_name': 'PertanyaanSoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jawaban': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'materi_soal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['belajar.MateriSoal']", 'symmetrical': 'False'}),
            'soal': ('django.db.models.fields.TextField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'system.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'alamat': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kelamin': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nama_lengkap': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tempat_lahir': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tgl_daftar': ('django.db.models.fields.DateField', [], {}),
            'tgl_lahir': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['belajar']

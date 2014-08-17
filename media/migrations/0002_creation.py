# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Upload'
        db.create_table(u'media_upload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'media', ['Upload'])

        # Adding model 'File'
        db.create_table(u'media_file', (
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('upload', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['media.Upload'])),
        ))
        db.send_create_signal(u'media', ['File'])

        # Adding model 'Record'
        db.create_table(u'media_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barcode', self.gf('django.db.models.fields.IntegerField')()),
            ('contenttype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('releasedate', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('upload', self.gf('django.db.models.fields.related.ForeignKey')(related_name='records', to=orm['media.Upload'])),
        ))
        db.send_create_signal(u'media', ['Record'])


    def backwards(self, orm):
        # Deleting model 'File'
        db.delete_table(u'media_media')

        # Deleting model 'Record'
        db.delete_table(u'media_record')

        # Deleting model 'Upload'
        db.delete_table(u'media_upload')


    models = {
        u'media.file': {
            'Meta': {'object_name': 'File'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['media.Upload']"})
        },
        u'media.record': {
            'Meta': {'object_name': 'Record'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'releasedate': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': u"orm['media.Upload']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'media.upload': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Upload'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['media']

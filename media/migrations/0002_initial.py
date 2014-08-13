# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manifest'
        db.create_table(u'media_manifest', (
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'media', ['Manifest'])

        # Adding model 'MediaData'
        db.create_table(u'media_mediadata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barcode', self.gf('django.db.models.fields.IntegerField')()),
            ('contenttype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('releasedate', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('manifest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media', to=orm['media.Manifest'])),
        ))
        db.send_create_signal(u'media', ['MediaData'])

        # Adding model 'Media'
        db.create_table(u'media_media', (
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('data', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['media.MediaData'])),
        ))
        db.send_create_signal(u'media', ['Media'])

        # Adding model 'Upload'
        db.create_table(u'media_upload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('manifest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uploads', to=orm['media.Manifest'])),
        ))
        db.send_create_signal(u'media', ['Upload'])


    def backwards(self, orm):
        # Deleting model 'Manifest'
        db.delete_table(u'media_manifest')

        # Deleting model 'MediaData'
        db.delete_table(u'media_mediadata')

        # Deleting model 'Media'
        db.delete_table(u'media_media')

        # Deleting model 'Upload'
        db.delete_table(u'media_upload')


    models = {
        u'media.manifest': {
            'Meta': {'object_name': 'Manifest'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'data': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['media.MediaData']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        u'media.mediadata': {
            'Meta': {'object_name': 'MediaData'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['media.Manifest']"}),
            'releasedate': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'media.upload': {
            'Meta': {'object_name': 'Upload'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploads'", 'to': u"orm['media.Manifest']"})
        }
    }

    complete_apps = ['media']
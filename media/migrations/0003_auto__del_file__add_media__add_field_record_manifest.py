# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'File'
        db.delete_table(u'media_file')

        # Adding model 'Media'
        db.create_table(u'media_media', (
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('upload', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media', to=orm['media.Upload'])),
        ))
        db.send_create_signal(u'media', ['Media'])

        # Adding field 'Record.manifest'
        db.add_column(u'media_record', 'manifest',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='records', to=orm['media.Media']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'File'
        db.create_table(u'media_file', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('upload', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['media.Upload'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
        ))
        db.send_create_signal(u'media', ['File'])

        # Deleting model 'Media'
        db.delete_table(u'media_media')

        # Deleting field 'Record.manifest'
        db.delete_column(u'media_record', 'manifest_id')


    models = {
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['media.Upload']"})
        },
        u'media.record': {
            'Meta': {'object_name': 'Record'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': u"orm['media.Media']"}),
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
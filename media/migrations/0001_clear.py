# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FileInstance'
        db.delete_table(u'media_fileinstance')

        # Deleting model 'Manifest'
        db.delete_table(u'media_manifest')

        # Deleting model 'MediaData'
        db.delete_table(u'media_mediadata')

        # Deleting model 'Media'
        db.delete_table(u'media_media')

        # Deleting model 'Upload'
        db.delete_table(u'media_upload')


    def backwards(self, orm):
        pass


    models = {
        u'media.fileinstance': {
            'Meta': {'object_name': 'FileInstance'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'})
        },
        u'media.manifest': {
            'Meta': {'object_name': 'Manifest', '_ormbases': [u'media.FileInstance']},
            u'fileinstance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['media.FileInstance']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'media.media': {
            'Meta': {'object_name': 'Media', '_ormbases': [u'media.FileInstance']},
            'data': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['media.MediaData']"}),
            u'fileinstance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['media.FileInstance']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'media.mediadata': {
            'Meta': {'object_name': 'MediaData'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['media.Manifest']"}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
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
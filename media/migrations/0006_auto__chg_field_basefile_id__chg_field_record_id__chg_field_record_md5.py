# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BaseFile.id'
        db.alter_column(u'media_basefile', 'id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True))

        # Changing field 'Record.id'
        db.alter_column(u'media_record', 'id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True))

        # Changing field 'Record.md5'
        db.alter_column(u'media_record', 'md5', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'BaseFile.id'
        db.alter_column(u'media_basefile', 'id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True))

        # Changing field 'Record.id'
        db.alter_column(u'media_record', 'id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True))

        # Changing field 'Record.md5'
        db.alter_column(u'media_record', 'md5', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        u'media.basefile': {
            'Meta': {'object_name': 'BaseFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        u'media.manifestfile': {
            'Meta': {'object_name': 'ManifestFile', '_ormbases': [u'media.BaseFile']},
            u'basefile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['media.BaseFile']", 'unique': 'True', 'primary_key': 'True'}),
            'upload': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'manifests'", 'symmetrical': 'False', 'to': u"orm['media.Upload']"})
        },
        u'media.mediafile': {
            'Meta': {'object_name': 'MediaFile', '_ormbases': [u'media.BaseFile']},
            u'basefile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['media.BaseFile']", 'unique': 'True', 'primary_key': 'True'}),
            'upload': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'media'", 'symmetrical': 'False', 'to': u"orm['media.Upload']"})
        },
        u'media.record': {
            'Meta': {'object_name': 'Record'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'records'", 'symmetrical': 'False', 'to': u"orm['media.ManifestFile']"}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'null': 'True', 'to': u"orm['media.MediaFile']"}),
            'releasedate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'media.upload': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Upload'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['media']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Media.md5'
        db.delete_column(u'media_media', 'md5')

        # Adding field 'Media.id'
        db.add_column(u'media_media', 'id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=32, primary_key=True),
                      keep_default=False)


        # Changing field 'Record.id'
        db.alter_column(u'media_record', 'id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True))

    def backwards(self, orm):
        # Adding field 'Media.md5'
        db.add_column(u'media_media', 'md5',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=32, primary_key=True),
                      keep_default=False)

        # Deleting field 'Media.id'
        db.delete_column(u'media_media', 'id')


        # Changing field 'Record.id'
        db.alter_column(u'media_record', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['media.Upload']"})
        },
        u'media.record': {
            'Meta': {'object_name': 'Record'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
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
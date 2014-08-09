# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Media.md5'
        db.add_column(u'media_media', 'md5',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Media.md5'
        db.delete_column(u'media_media', 'md5')


    models = {
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'releasedate': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['media']
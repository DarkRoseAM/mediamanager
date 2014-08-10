# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

ADD_COLUMNS = {
    'barcode': 'django.db.models.fields.IntegerField',
    'contenttype': 'django.db.models.fields.CharField',
    'language': 'django.db.models.fields.CharField',
    'md5': 'django.db.models.fields.CharField',
    'releasedate': 'django.db.models.fields.DateField',
    'version': 'django.db.models.fields.CharField',
}

DELETE_COLUMNS = {
    'content': 'django.db.models.fields.TextField',
    'created_at': 'django.db.models.fields.DateTimeField',
    'published': 'django.db.models.fields.BooleanField',
    'updated_at': 'django.db.models.fields.DateTimeField',
}


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding fields.
        for col, fieldType in ADD_COLUMNS.iteritems():
            try:
                db.add_column(
                    'media_media',
                    col,
                    self.gf(fieldType)(),
                )
            except:
                pass

        # Deleting fields.
        for col in DELETE_COLUMNS.keys():
            try:
                db.delete_column('media_media', col)
            except:
                pass

    def backwards(self, orm):
        # Adding fields.
        for col, fieldType in DELETE_COLUMNS.iteritems():
            try:
                db.add_column(
                    'media_media',
                    col,
                    self.gf(fieldType)(),
                )
            except:
                pass

        # Deleting fields.
        for col in ADD_COLUMNS.keys():
            try:
                db.delete_column('media_media', col)
            except:
                pass

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
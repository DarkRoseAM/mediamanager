# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Media'
        db.create_table(u'media_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('releasedate', self.gf('django.db.models.fields.DateField')()),
            ('contenttype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('barcode', self.gf('django.db.models.fields.IntegerField')()),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'media', ['Media'])


    def backwards(self, orm):
        # Deleting model 'Media'
        db.delete_table(u'media_media')


    models = {
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'releasedate': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['media']
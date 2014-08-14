# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileInstance'
        db.create_table(u'media_fileinstance', (
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'media', ['FileInstance'])

        # Deleting field 'Media.file'
        db.delete_column(u'media_media', 'file')

        # Deleting field 'Media.md5'
        db.delete_column(u'media_media', 'md5')

        # Adding field 'Media.fileinstance_ptr'
        db.add_column(u'media_media', u'fileinstance_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['media.FileInstance'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Manifest.file'
        db.delete_column(u'media_manifest', 'file')

        # Deleting field 'Manifest.md5'
        db.delete_column(u'media_manifest', 'md5')

        # Adding field 'Manifest.fileinstance_ptr'
        db.add_column(u'media_manifest', u'fileinstance_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['media.FileInstance'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FileInstance'
        db.delete_table(u'media_fileinstance')

        # Adding field 'Media.file'
        db.add_column(u'media_media', 'file',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Media.md5'
        db.add_column(u'media_media', 'md5',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255, primary_key=True),
                      keep_default=False)

        # Deleting field 'Media.fileinstance_ptr'
        db.delete_column(u'media_media', u'fileinstance_ptr_id')

        # Adding field 'Manifest.file'
        db.add_column(u'media_manifest', 'file',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Manifest.md5'
        db.add_column(u'media_manifest', 'md5',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255, primary_key=True),
                      keep_default=False)

        # Deleting field 'Manifest.fileinstance_ptr'
        db.delete_column(u'media_manifest', u'fileinstance_ptr_id')


    models = {
        u'media.fileinstance': {
            'Meta': {'object_name': 'FileInstance'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
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
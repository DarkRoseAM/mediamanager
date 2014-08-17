# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ManifestFile'
        db.create_table(u'media_manifestfile', (
            (u'basefile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['media.BaseFile'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'media', ['ManifestFile'])

        # Adding M2M table for field upload on 'ManifestFile'
        m2m_table_name = db.shorten_name(u'media_manifestfile_upload')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manifestfile', models.ForeignKey(orm[u'media.manifestfile'], null=False)),
            ('upload', models.ForeignKey(orm[u'media.upload'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manifestfile_id', 'upload_id'])

        # Adding model 'BaseFile'
        db.create_table(u'media_basefile', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'media', ['BaseFile'])

        # Adding model 'Record'
        db.create_table(u'media_record', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('barcode', self.gf('django.db.models.fields.IntegerField')()),
            ('contenttype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('releasedate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'media', ['Record'])

        # Adding M2M table for field manifest on 'Record'
        m2m_table_name = db.shorten_name(u'media_record_manifest')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'media.record'], null=False)),
            ('manifestfile', models.ForeignKey(orm[u'media.manifestfile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['record_id', 'manifestfile_id'])

        # Adding model 'Upload'
        db.create_table(u'media_upload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'media', ['Upload'])

        # Adding model 'MediaFile'
        db.create_table(u'media_mediafile', (
            (u'basefile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['media.BaseFile'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'media', ['MediaFile'])

        # Adding M2M table for field upload on 'MediaFile'
        m2m_table_name = db.shorten_name(u'media_mediafile_upload')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediafile', models.ForeignKey(orm[u'media.mediafile'], null=False)),
            ('upload', models.ForeignKey(orm[u'media.upload'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mediafile_id', 'upload_id'])


    def backwards(self, orm):
        # Deleting model 'ManifestFile'
        db.delete_table(u'media_manifestfile')

        # Removing M2M table for field upload on 'ManifestFile'
        db.delete_table(db.shorten_name(u'media_manifestfile_upload'))

        # Deleting model 'BaseFile'
        db.delete_table(u'media_basefile')

        # Deleting model 'Record'
        db.delete_table(u'media_record')

        # Removing M2M table for field manifest on 'Record'
        db.delete_table(db.shorten_name(u'media_record_manifest'))

        # Deleting model 'Upload'
        db.delete_table(u'media_upload')

        # Deleting model 'MediaFile'
        db.delete_table(u'media_mediafile')

        # Removing M2M table for field upload on 'MediaFile'
        db.delete_table(db.shorten_name(u'media_mediafile_upload'))


    models = {
        u'media.basefile': {
            'Meta': {'object_name': 'BaseFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'})
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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'records'", 'symmetrical': 'False', 'to': u"orm['media.ManifestFile']"}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
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
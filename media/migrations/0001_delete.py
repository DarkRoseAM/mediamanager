# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BaseFile'
        db.delete_table(u'media_basefile')

        # Deleting model 'ManifestFile'
        db.delete_table(u'media_manifestfile')

        # Deleting model 'MediaFile'
        db.delete_table(u'media_mediafile')

        # Deleting model 'Record'
        #db.delete_table(u'media_record')

        # Deleting model 'Upload'
        db.delete_table(u'media_upload')

    def backwards(self, orm):
        pass


    models = {}

    complete_apps = ['media']
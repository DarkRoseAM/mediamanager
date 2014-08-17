# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'M2M'
        db.delete_table(u'media_manifestfile_upload')

        # Deleting model 'M2M'
        db.delete_table(u'media_mediafile_upload')

        # Deleting model 'M2M'
        db.delete_table(u'media_record_manifest')

    def backwards(self, orm):
        pass


    models = {}

    complete_apps = ['media']
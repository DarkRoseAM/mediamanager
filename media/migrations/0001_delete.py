# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BaseFile'
        db.delete_table(u'media_media')

    def backwards(self, orm):
        pass


    models = {}

    complete_apps = ['media']
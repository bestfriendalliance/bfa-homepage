# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HomepageLearnMoreLink.slug'
        db.delete_column(u'bfa_homepage_homepagelearnmorelink', 'slug')

        # Adding field 'HomepageLearnMoreLink.url'
        db.add_column(u'bfa_homepage_homepagelearnmorelink', 'url',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'HomepageLearnMoreLink.slug'
        db.add_column(u'bfa_homepage_homepagelearnmorelink', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=40),
                      keep_default=False)

        # Deleting field 'HomepageLearnMoreLink.url'
        db.delete_column(u'bfa_homepage_homepagelearnmorelink', 'url')


    models = {
        u'bfa_homepage.homepagelearnmorelink': {
            'Meta': {'object_name': 'HomepageLearnMoreLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bfa_homepage']
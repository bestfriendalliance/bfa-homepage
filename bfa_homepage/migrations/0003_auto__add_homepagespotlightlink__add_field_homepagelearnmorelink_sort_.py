# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomepageSpotlightLink'
        db.create_table(u'bfa_homepage_homepagespotlightlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sort_order', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'bfa_homepage', ['HomepageSpotlightLink'])

        # Adding field 'HomepageLearnMoreLink.sort_order'
        db.add_column(u'bfa_homepage_homepagelearnmorelink', 'sort_order',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'HomepageSpotlightLink'
        db.delete_table(u'bfa_homepage_homepagespotlightlink')

        # Deleting field 'HomepageLearnMoreLink.sort_order'
        db.delete_column(u'bfa_homepage_homepagelearnmorelink', 'sort_order')


    models = {
        u'bfa_homepage.homepagelearnmorelink': {
            'Meta': {'object_name': 'HomepageLearnMoreLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bfa_homepage.homepagespotlightlink': {
            'Meta': {'object_name': 'HomepageSpotlightLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bfa_homepage']
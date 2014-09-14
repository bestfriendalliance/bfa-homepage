# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomepageLearnMoreLink'
        db.create_table(u'bfa_homepage_homepagelearnmorelink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('icon_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'bfa_homepage', ['HomepageLearnMoreLink'])


    def backwards(self, orm):
        # Deleting model 'HomepageLearnMoreLink'
        db.delete_table(u'bfa_homepage_homepagelearnmorelink')


    models = {
        u'bfa_homepage.homepagelearnmorelink': {
            'Meta': {'object_name': 'HomepageLearnMoreLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['bfa_homepage']
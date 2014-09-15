# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomepageTestimonial'
        db.create_table(u'bfa_homepage_homepagetestimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('sort_order', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bfa_homepage', ['HomepageTestimonial'])

        # Adding field 'HomepageSpotlightLink.show'
        db.add_column(u'bfa_homepage_homepagespotlightlink', 'show',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HomepageLearnMoreLink.show'
        db.add_column(u'bfa_homepage_homepagelearnmorelink', 'show',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'HomepageTestimonial'
        db.delete_table(u'bfa_homepage_homepagetestimonial')

        # Deleting field 'HomepageSpotlightLink.show'
        db.delete_column(u'bfa_homepage_homepagespotlightlink', 'show')

        # Deleting field 'HomepageLearnMoreLink.show'
        db.delete_column(u'bfa_homepage_homepagelearnmorelink', 'show')


    models = {
        u'bfa_homepage.homepagelearnmorelink': {
            'Meta': {'object_name': 'HomepageLearnMoreLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bfa_homepage.homepagespotlightlink': {
            'Meta': {'object_name': 'HomepageSpotlightLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bfa_homepage.homepagetestimonial': {
            'Meta': {'object_name': 'HomepageTestimonial'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bfa_homepage']
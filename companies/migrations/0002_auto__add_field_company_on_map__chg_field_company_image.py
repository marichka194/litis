# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company.on_map'
        db.add_column(u'companies_company', 'on_map',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Company.image'
        db.alter_column(u'companies_company', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'Company.on_map'
        db.delete_column(u'companies_company', 'on_map')


        # User chose to not deal with backwards NULL issues for 'Company.image'
        raise RuntimeError("Cannot reverse this migration. 'Company.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.image'
        db.alter_column(u'companies_company', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'companies.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        u'companies.company': {
            'Meta': {'ordering': "['rating', 'name']", 'object_name': 'Company'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'on_map': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.SubCategory']"})
        },
        u'companies.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        }
    }

    complete_apps = ['companies']
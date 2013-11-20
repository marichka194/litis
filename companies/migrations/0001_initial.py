# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'companies_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
        ))
        db.send_create_signal(u'companies', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'companies_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Category'])),
        ))
        db.send_create_signal(u'companies', ['SubCategory'])

        # Adding model 'Company'
        db.create_table(u'companies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.SubCategory'])),
        ))
        db.send_create_signal(u'companies', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'companies_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'companies_subcategory')

        # Deleting model 'Company'
        db.delete_table(u'companies_company')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.cell_phone'
        db.add_column('students_student', 'cell_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Student.zipcode'
        db.add_column('students_student', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Student.city'
        db.add_column('students_student', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.cell_phone'
        db.delete_column('students_student', 'cell_phone')

        # Deleting field 'Student.zipcode'
        db.delete_column('students_student', 'zipcode')

        # Deleting field 'Student.city'
        db.delete_column('students_student', 'city')


    models = {
        'students.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': "orm['students.Student']"})
        },
        'students.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'students.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Ethnicity']"}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'MA'", 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['students']
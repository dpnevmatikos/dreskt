# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Grade.course'
        db.add_column('students_grade', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='course', to=orm['students.Course']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Grade.course'
        db.delete_column('students_grade', 'course_id')


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
        'students.grade': {
            'Meta': {'object_name': 'Grade'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course'", 'to': "orm['students.Course']"}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student'", 'to': "orm['students.Student']"})
        },
        'students.notification': {
            'Meta': {'object_name': 'Notification'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 29, 0, 0)'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'})
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
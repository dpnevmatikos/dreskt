# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.birthday'
        db.add_column('students_student', 'birthday',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 8, 27, 0, 0)),
                      keep_default=False)

        # Adding field 'Student.gender'
        db.add_column('students_student', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='MA', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.birthday'
        db.delete_column('students_student', 'birthday')

        # Deleting field 'Student.gender'
        db.delete_column('students_student', 'gender')


    models = {
        'students.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': "orm['students.Student']"})
        },
        'students.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'MA'", 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['students']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('students_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('students', ['Student'])

        # Adding model 'Course'
        db.create_table('students_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('students', ['Course'])

        # Adding M2M table for field students on 'Course'
        db.create_table('students_course_students', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['students.course'], null=False)),
            ('student', models.ForeignKey(orm['students.student'], null=False))
        ))
        db.create_unique('students_course_students', ['course_id', 'student_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('students_student')

        # Deleting model 'Course'
        db.delete_table('students_course')

        # Removing M2M table for field students on 'Course'
        db.delete_table('students_course_students')


    models = {
        'students.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['students.Student']", 'symmetrical': 'False'})
        },
        'students.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['students']
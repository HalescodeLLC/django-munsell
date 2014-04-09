# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MunsellColor'
        db.create_table('mcolor_munsellcolor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hue_a', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('hue_b', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('chroma', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('nice_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('munsell_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('sortable_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('n_r', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('n_g', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('n_b', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('s_r', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('s_g', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('s_b', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('hexval', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('mcolor', ['MunsellColor'])


    def backwards(self, orm):
        # Deleting model 'MunsellColor'
        db.delete_table('mcolor_munsellcolor')


    models = {
        'mcolor.munsellcolor': {
            'Meta': {'object_name': 'MunsellColor'},
            'chroma': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'hexval': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'hue_a': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'hue_b': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'munsell_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'n_b': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'n_g': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'n_r': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'nice_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            's_b': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            's_g': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            's_r': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'sortable_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['mcolor']
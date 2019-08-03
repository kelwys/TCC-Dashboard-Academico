# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DimAluno(models.Model):
    iddim_aluno = models.AutoField(db_column='idDim_aluno', primary_key=True)  # Field name made lowercase.
    nome_pessoa = models.CharField(max_length=100, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_aluno'


class DimAvaliacao(models.Model):
    iddim_avaliacao = models.AutoField(db_column='idDim_avaliacao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_avaliacao'


class DimDisciplina(models.Model):
    iddim_disciplina = models.AutoField(db_column='idDim_disciplina', primary_key=True)  # Field name made lowercase.
    codigo_disciplina = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_disciplina'


class DimFrequencia(models.Model):
    iddim_frequencia = models.AutoField(db_column='idDim_frequencia', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_frequencia'


class DimGrupoavaliacao(models.Model):
    iddim_grupoavaliacao = models.AutoField(db_column='idDim_grupoAvaliacao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_grupoAvaliacao'


class DimNota(models.Model):
    iddim_nota = models.AutoField(db_column='idDim_nota', primary_key=True)  # Field name made lowercase.
    nota = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_nota'


class DimPauta(models.Model):
    iddim_pauta = models.AutoField(db_column='idDim_pauta', primary_key=True)  # Field name made lowercase.
    identificador = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_pauta'


class DimPeriodo(models.Model):
    iddim_periodo = models.AutoField(db_column='idDim_periodo', primary_key=True)  # Field name made lowercase.
    ano = models.IntegerField(blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_periodo'


class DimProfessor(models.Model):
    iddim_professor = models.AutoField(db_column='idDim_professor', primary_key=True)  # Field name made lowercase.
    nome_pessoa = models.CharField(max_length=100, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_professor'


class DimTurmadeingresso(models.Model):
    iddim_turmadeingresso = models.AutoField(db_column='idDim_turmaDeIngresso', primary_key=True)  # Field name made lowercase.
    # idwac_turmadeingresso = models.IntegerField(db_column='idWac_turmadeingresso', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45, blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim_turmaDeIngresso'


class FatoAbsenteismo(models.Model):
    idfato_absenteismo = models.IntegerField(db_column='idFato_absenteismo', primary_key=True)  # Field name made lowercase.
    dim_frequencia_iddim_frequencia = models.ForeignKey(DimFrequencia, db_column='Dim_frequencia_idDim_frequencia')  # Field name made lowercase.
    dim_professor_iddim_professor = models.ForeignKey(DimProfessor, db_column='Dim_professor_idDim_professor')  # Field name made lowercase.
    dim_aluno_iddim_aluno = models.ForeignKey(DimAluno, db_column='Dim_aluno_idDim_aluno')  # Field name made lowercase.
    dim_periodo_iddim_periodo = models.ForeignKey(DimPeriodo, db_column='Dim_periodo_idDim_periodo')  # Field name made lowercase.
    dim_grupoavaliacao_iddim_grupoavaliacao = models.ForeignKey(DimGrupoavaliacao, db_column='Dim_grupoAvaliacao_idDim_grupoAvaliacao')  # Field name made lowercase.
    dim_turmadeingresso_iddim_turmadeingresso = models.ForeignKey(DimTurmadeingresso, db_column='Dim_turmaDeIngresso_idDim_turmaDeIngresso')  # Field name made lowercase.
    dim_pauta_iddim_pauta = models.ForeignKey(DimPauta, db_column='Dim_pauta_idDim_pauta')  # Field name made lowercase.
    dim_disciplina_iddim_disciplina = models.ForeignKey(DimDisciplina, db_column='Dim_disciplina_idDim_disciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fato_absenteismo'


class FatoDesempenhoaluno(models.Model):
    idfato_desempenhoaluno = models.IntegerField(db_column='idFato_desempenhoAluno', primary_key=True)  # Field name made lowercase.
    media = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    media_n1 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    media_n2 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    media_n3 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dim_aluno_iddim_aluno = models.ForeignKey(DimAluno, db_column='Dim_aluno_idDim_aluno')  # Field name made lowercase.
    dim_professor_iddim_professor = models.ForeignKey(DimProfessor, db_column='Dim_professor_idDim_professor')  # Field name made lowercase.
    dim_periodo_iddim_periodo = models.ForeignKey(DimPeriodo, db_column='Dim_periodo_idDim_periodo')  # Field name made lowercase.
    dim_grupoavaliacao_iddim_grupoavaliacao = models.ForeignKey(DimGrupoavaliacao, db_column='Dim_grupoAvaliacao_idDim_grupoAvaliacao')  # Field name made lowercase.
    dim_nota_iddim_nota = models.ForeignKey(DimNota, db_column='Dim_nota_idDim_nota')  # Field name made lowercase.
    dim_turmadeingresso_iddim_turmadeingresso = models.ForeignKey(DimTurmadeingresso, db_column='Dim_turmaDeIngresso_idDim_turmaDeIngresso')  # Field name made lowercase.
    dim_pauta_iddim_pauta = models.ForeignKey(DimPauta, db_column='Dim_pauta_idDim_pauta')  # Field name made lowercase.
    dim_disciplina_iddim_disciplina = models.ForeignKey(DimDisciplina, db_column='Dim_disciplina_idDim_disciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fato_desempenhoAluno'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

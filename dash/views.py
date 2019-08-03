from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .models import *
import numpy as np
import json
from django.core.serializers.json import DjangoJSONEncoder
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


def gerajson(request):

    periodo = DimPeriodo.objects.all().values_list('ano',flat=True)
    professor = DimProfessor.objects.filter(iddim_professor__in=FatoDesempenhoaluno.objects.all().values(
        'dim_professor_iddim_professor')).order_by('nome_pessoa')
    disciplina = DimDisciplina.objects.filter(iddim_disciplina__in=FatoDesempenhoaluno.objects.all().values(
        'dim_disciplina_iddim_disciplina')).order_by('nome')
    turma = DimTurmadeingresso.objects.filter(iddim_turmadeingresso__in=FatoDesempenhoaluno.objects.all().values(
        'dim_turmadeingresso_iddim_turmadeingresso')).order_by('descricao')
    print(request.POST)

    nota=FatoDesempenhoaluno.objects.filter(dim_turmadeingresso_iddim_turmadeingresso=1072).values_list(
        'media_n1', 'media_n2', 'media_n3').distinct()
    if request.POST:
        notaset = FatoDesempenhoaluno.objects.filter(dim_turmadeingresso_iddim_turmadeingresso=request.POST.get(
            'turma')).values_list('media_n1', 'media_n2', 'media_n3').distinct().filter(dim_disciplina_iddim_disciplina=request.POST.get(
            'disciplina')).values_list('media_n1', 'media_n2', 'media_n3').distinct().filter(dim_professor_iddim_professor=request.POST.get(
            'professor')).values_list('media_n1', 'media_n2', 'media_n3').distinct()
        if len(notaset) > 0:
            nota = notaset


    falta=0
    if request.POST:
        faltaset = FatoAbsenteismo.objects.filter(dim_turmadeingresso_iddim_turmadeingresso=request.POST.get(
            'turma')).values_list('falta').distinct().filter(dim_disciplina_iddim_disciplina=request.POST.get(
            'disciplina')).values_list('falta').distinct().filter(dim_professor_iddim_professor=request.POST.get(
            'professor')).values_list('qtd_falta').distinct()
        if len(faltaset) > 0:
            falta = faltaset

    print(request.POST.get('turma'))
    nota_json = json.dumps(nota[0], cls=DecimalEncoder)
    falta_json = json.dumps(falta[0], cls=DjangoJSONEncoder)
    print(nota_json)


    context = dict(disciplina = disciplina, turma = turma, nota = nota_json, falta = falta_json, turmapost = request.POST.get('turma'))
    c = RequestContext(request, context)
    return render_to_response('dashboard.html', c)


def sobre(request):
    return render_to_response('blank.html')
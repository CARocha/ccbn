# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import get_model
from django.template import RequestContext
from sistema.models import Salida
from models import *
from registro.models import *
from registro.forms import *

def testing(request):
    id = request.GET.get('id', 1)
    salida = Salida.objects.get(id=id)
    app_label, model = salida.model.split(',')
    model = get_model(app_label, model)
    query = model.objects.all()

    if salida.tipo_meta == 1: # percent
        pass
    elif salida.tipo_meta == 2: # count
        tipo_meta = query.count()

    return render_to_response('index2.html', RequestContext(request, locals()))


def _query_set_filtrado(request):
    params = {}
    if request.session['sexo']:
        params['sexo'] = request.session['sexo']
        
    if request.session['edad1']:
        edad1 = int(request.session['edad1'])
    if request.session['edad2']:
        edad2 = int(request.session['edad2']) 

    encuestas = Persona.objects.filter( ** params)

    return encuestas

def consultar(request):
    if request.method == 'POST':
        form = ChatelEdad(request.POST)
        if form.is_valid():
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['edad1'] = form.cleaned_data['edad1']
            request.session['edad2'] = form.cleaned_data['edad2']
           
    else:
        form = ChatelEdad()       
    return render_to_response('consultar.html', RequestContext(request, locals()))


def filtrado_chatel(request):
    fichas = _query_set_filtrado(request)
    #print request.session['edad1']
    #print request.session['edad2']
    lista = []
    for k in fichas:
        if k.edad_chatel() in range(request.session['edad1'],request.session['edad2']+1):
            lista.append(k)
    
    #lista_barrio = {}
    #for barrio in Barrio.objects.all():
        #lista_barrio[barrio] = lista.objects.filter(barrio=barrio).count()
    print dir(lista)
    return render_to_response('edad.html', RequestContext(request, locals()))
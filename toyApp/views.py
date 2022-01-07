from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from toyApp.processer import CommandProcesser, sender_array
from toyApp.errors import FirstParameterError

def show_index(request):
    """ Carrega a página do jogo """
    return render(request, 'index.html')

@csrf_exempt
def process_commands(request):
    """ processa os comandos da página web """
    if request.method == 'POST':
        try:
            p = CommandProcesser()
            v = p.validate_commands()
            list_commands = request.POST.get('commands').split('\n')

            sender_array(list_commands, v)
            return HttpResponse(p.report())
        except FirstParameterError as e:
            return HttpResponse(json.dumps({"error": e.message }))
    return HttpResponse(status=401)
import os
import time 

from django.core.management.base import BaseCommand
from toyApp.processer import CommandProcesser, sender
from toyApp.errors import FirstParameterError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help="O Caminho do arquivo com a lista de comandos a serem processados")

    def handle(self, *args, **kwargs):
        
        filepath = kwargs['filepath']
        try:
            p = CommandProcesser()
            v = p.validate_commands()
            sender(filepath, v)
        except FirstParameterError as e:
            pass
        
        
        
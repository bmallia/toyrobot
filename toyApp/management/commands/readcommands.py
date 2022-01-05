import os
import time 

from django.core.management.base import BaseCommand
from toyApp.processer import validation_commands

class CommandProcesser(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help="O Caminho do arquivo com a lista de comandos a serem processados")

    def handle(self, *args, **kwargs):
        
        filepath = kwargs['filepath']
        validation_commands(['PLACE', 'LEFT', 'RIGHT']) 
        
        
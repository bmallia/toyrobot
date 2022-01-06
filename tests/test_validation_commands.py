import pytest
import os
from toyApp.processer import sender, CommandProcesser


def test_parameter_list_command_example_a():
    """ Criação de teste de lista de comandos da referente ao arquivo B """
    filename = os.path.dirname(__file__) + "/list_commands_a.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)
    assert p.report() == "0,1,SOUTH"

def test_parameter_list_command_example_b():
    """ Criação de teste de lista de comandos da referente ao arquivo B """
    filename = os.path.dirname(__file__) + "/list_commands_b.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)
    assert p.report() == "0,0,EAST"

def test_parameter_list_command_example_c():
    """ Criação de teste de lista de comandos da referente ao arquivo C """
    filename = os.path.dirname(__file__) + "/list_commands_c.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)    
    assert p.report() == "3,3,SOUTH"

def test_parameter_list_command_across_board():
    """ Criação de teste que simula a tentativa de ultrapassar o limite do tabuleiro """
    filename = os.path.dirname(__file__) + "/list_commands_d.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)    
    assert p.report() == "3,4,SOUTH"
    
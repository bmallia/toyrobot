import pytest
import os
from toyApp.processer import sender, CommandProcesser


def test_parameter_list_command_example_a():
    filename = os.path.dirname(__file__) + "/list_commands_a.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)
    assert p.report() == "0,1,SOUTH"

def test_parameter_list_command_example_b():
    filename = os.path.dirname(__file__) + "/list_commands_b.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)
    assert p.report() == "0,0,EAST"

def test_parameter_list_command_example_c():
    filename = os.path.dirname(__file__) + "/list_commands_c.txt"

    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename, v)    
    assert p.report() == "3,3,SOUTH"

import pytest
import os
from toyApp.processer import sender, CommandProcesser

@pytest.fixture(scope="session")
def filename_commands():
    return os.path.dirname(__file__) + "/list_commands.txt"

def test_parameter_list_command_valid(filename_commands):
    p = CommandProcesser()
    v = p.validate_commands()

    sender(filename_commands, v)    
    assert str(p) == "3,3,SOUTH"
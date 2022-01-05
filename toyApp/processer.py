import re

from toyApp.decorators import coroutine_decorator
from toyApp.commands import ValidCommands


def sender(filename, target):
    """
       Lê o arquivo e manda cada linha para ser validada

    Args:
        filename: caminho do arquivo a ser lide
        target: coroutine que vai validar as linhas de comando

    """     
    for line in open(filename):
        t = target.send(line)
        ##target.__next__()
    target.close()
    


    

class CommandProcesser:

    """ Classe que representa o processador de comandos """

    pattern = re.compile("PLACE (\d),(\d),(EAST|SOUTH|NORTH|WEST)")

    def __init__(self):
        self.coord = (0,0)
        self.direction = None

    def place(self, x, y, direction):
        self.coord = (x, y)
        self.direction = direction

    def move(self):
        """ Adiciona movimento de acordo com a direção corrente """
        pass
    
    def __validate_table__(self, coord):
        """ Valida se as coordenadas estão no tabuleiro

        Args:
            coord ([type]): [description]
        """
        pass

    def __str__(self):
        """ """
        return f"{self.coord[0]},{self.coord[1]} {self.direction}"

    @coroutine_decorator
    def validate_commands(self):
        """
            Valida cada linha de comando passado como parâmetro se é válido.
            A primeira linha precisa ser o comando PLACE

        Args:
            string ([type]): [description]
        """
        count_line = 1

        try:
            while True:
                line = yield
                if count_line == 1:
                    if self.pattern.match(line):
                        print(f"Comando {line} sendo executado")
                        parameters = self.pattern.search(line)
                        self.place(int(parameters.group(1)), int(parameters.group(2)), parameters.group(3))
                        print(f"Comando {line} executado com sucesso!")
                    else:
                        print("A primeira linha deve conter o comando PLACE")                    
                        raise GeneratorExit("A primeira linha deve conter o comando PLACE")                


                ##trata os outros comandos
                command_found_list = [e.value for e in ValidCommands if e.value in line]
                if len(command_found_list) == 0:
                    print(f"o Comando {line} é inválido")

                count_line += 1


        except GeneratorExit as e:
            print(f"iteração concluída, foi lida até a linha {count_line}")

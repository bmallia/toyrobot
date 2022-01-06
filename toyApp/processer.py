import re
import collections 
from toyApp.decorators import coroutine_decorator
from toyApp.commands import ValidCommands, Directions


def sender(filename, target):
    """
       Lê o arquivo e manda cada linha para ser validada

    Args:
        filename: caminho do arquivo a ser lide
        target: coroutine que vai validar as linhas de comando

    """     
    for line in open(filename):
        t = target.send(line)
    target.close()
    

class CommandProcesser:

    """ Classe que representa o processador de comandos """

    pattern = re.compile("PLACE (\d),(\d),(EAST|SOUTH|NORTH|WEST)")

    def __init__(self):
        coordenate = collections.namedtuple("Coordenadas", "x y")
        self.coord = coordenate(0,0)
        self.direction = None

    def place(self, x, y, direction):
        self.coord = self.coord._replace(x=x)
        self.coord = self.coord._replace(y=y)
        self.direction = direction

    def move(self):
        """ Adiciona movimento de acordo com a direção corrente """
        if self.direction == ValidCommands.SOUTH and self.coord.y < 4:
            self.coord = self.coord._replace(y=self.coord.y+1)
        elif self.direction == ValidCommands.EAST and self.coord.x < 4:
            self.coord = self.coord._replace(x=self.coord.x+1)
        

    def change_direction(self, direction):
        """ funão para mudar a direção """
        direct = [e for e in Directions if e.command == self.direction]
        new_direction = direct[0] + direction
        self.direction = new_direction.command
    
    def __validate_table__(self, coord):
        """ Valida se as coordenadas estão no tabuleiro

        Args:
            coord ([type]): [description]
        """
        pass

    def __str__(self):
        """ """
        return f"{self.coord[0]},{self.coord[1]},{self.direction.name}"

    def report(self):
        """ O comando REPORT retorna uma string com as coordenadas e a direção corrente """
        obj = str(self)
        print(obj)
        return obj


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
                line = line.replace('\n', '')

                if count_line == 1:
                    if self.pattern.match(line):
                        ##print(f"Comando {line} sendo executado") ##será o debug
                        parameters = self.pattern.search(line)
                        self.place(int(parameters.group(1)), int(parameters.group(2)), ValidCommands(parameters.group(3)))
                        ##print(f"Comando {line} executado com sucesso!") será o debug
                        count_line += 1
                        continue
                    else:                  
                        raise ValueError("A primeira linha deve conter o comando PLACE")                

                try:
                    ##trata os outros comandos
                    command = ValidCommands(line)
                except ValueError as e:
                    print(f"o Comando {line} é inválido")


                if line == ValidCommands.MOVE.value:
                    self.move()
                    count_line += 1
                    continue
                
                
                direction_found = [e for e in Directions if e.command == command]       
                if len(direction_found) != 0:
                    self.change_direction(direction_found[0])
                    count_line += 1
                    continue
                
                if line == ValidCommands.REPORT.value:
                    self.report()
                    count_line += 1
                    continue

        except GeneratorExit as e:
            ##print(f"iteração concluída, foi lida até a linha {count_line}")
            pass

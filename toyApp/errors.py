class FirstParameterError(ValueError):
    """ Classe que representa o erro quando o primeiro parametro da lista de comandos
    não é válido
    """
    def __init__(self, msg):
        self.message = msg
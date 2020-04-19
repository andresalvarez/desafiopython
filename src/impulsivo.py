from jogador import Jogador

class Impulsivo(Jogador):
    """
        Classe que sobrescreve o jogador para definir comportamento do jogador impulsivo
    """

    def __init__(self, nome):
        super().__init__(nome)

    def vai_comprar(self, valor, aluguel):  
        """
            O jogador impulsivo compra qualquer propriedade sobre a qual ele parar. se tiver saldo para comprar
        """    
        return (self.saldo - valor) >= 0
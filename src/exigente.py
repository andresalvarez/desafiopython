from jogador import Jogador

class Exigente(Jogador):
    """
        Classe que sobrescreve o jogador para definir comportamento do jogador exigente
    """

    def __init__(self, nome):
        super().__init__(nome)

    def vai_comprar(self, valor, aluguel):  
        """
            O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
        """    
        return aluguel > 50 and ((self.saldo - valor) >= 0)
      
    
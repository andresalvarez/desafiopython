from jogador import Jogador
import random as rnd

class Aleatorio(Jogador):
    """
        Classe que sobrescreve o jogador para definir comportamento do jogador aleatorio
    """

    def __init__(self, nome):
        super().__init__(nome)

    def vai_comprar(self, valor, aluguel):  
        """
            O jogador aleatório compra a propriedade que ele parar em cima com 
            probabilidade de 50%.
        """    
        
        return rnd.randint(0, 1) == 1 and ((self.saldo - valor) >= 0)
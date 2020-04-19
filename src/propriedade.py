class Propriedade:
    """
        Classe que define a propriedade
    """

    def __init__(self, nome, valor_Venda, valor_Aluguel):
        self.nome = nome
        self.valorDaVenda = valor_Venda
        self.valorDoAluguel = valor_Aluguel
        self.proprietario = None

    def vendida(self):
        """
            Retorna true se propridade tem proprietário
        """
        return self.proprietario != None

    def pertence(self,nome ):
        """
            Retorna true se propridade a um proprietario especifico
        """
        return None != self.proprietario and self.proprietario.nome == nome

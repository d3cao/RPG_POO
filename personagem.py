class personagem:

    def __init__(self, vida, dano, nome, xp, classe):
        self.vida = vida
        self.role = classe
        self.dano = dano
        self.nome = nome
        self.xp = xp
        self._vivo = True

    def ficha(self):
        print(f'Nome : {self.nome.ljust(20)}')
        print(f'Classe : {str(self.role).ljust(20)}')
        print(f'Vida : {str(self.vida).ljust(20)}')
        print(f'Dano : {str(self.dano).ljust(20)}')
        print(f'Experiência : {str(self.xp).ljust(20)}')

class arqueiro(personagem):
    def __init__(self, nome):
        self.role = 'Arqueiro'
        super().__init__(vida=100, dano=13, nome=nome, xp=12, classe = 'Arqueiro')

class mago(personagem):
    def __init__(self, nome):
        self.role = 'Mago'
        super().__init__(vida=80, dano=25, nome=nome, xp=13, classe = 'Mago')

class guerreiro(personagem):
    def __init__(self, nome):
        self.role = 'Guerreiro'
        super().__init__(vida = 120, dano = 15, nome = nome, xp = 10, classe = 'Guerreiro')
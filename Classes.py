class Programador:
    def __init__(self,nome, idade):
        self.nome = nome
        self.ferramenta_trabalho = None 
        self.idade = 20
        def getFerramenta(self):
            return self.ferramenta_trabalho
        
        def setFerramenta(self,ferramenta):
            self.ferramenta_trabalho = ferramenta

class Computador:
    def __init__(self,marca,processador):
        self.marca = marca
        self.processador = processador
    def getMarca(self):
        return self.marca
    
    def getProcessador(self):
        return self.processador
class Cell:
    def __init__ (self,marcaCell,processadorCell):
        self.marcaCell = marcaCell
        self.processadorCell = processadorCell
    
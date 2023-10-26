from Classes import *

funcionario = Programador("Carlos")
equipamento = Computador("Avell","intel core I5")
aparelho = Cell("samsung", "S22 Ultra")

funcionario.setferramenta(equipamento)
print(funcionario.getFerramenta().getmarca())
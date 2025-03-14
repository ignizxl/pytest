
# código fornecido na prova

def calcPontos(valorCompra, redex, cartaox):
  pontos = 0
  
  if redex and cartaox:
    pontos = valor * 3
  
  elif redex:
    pontos = valor * 1.5
  
  elif cartaox:
    pontos = valor
  
  return pontos
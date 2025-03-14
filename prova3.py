def calc_pontos(valor, redex, cartaox):
    if not isinstance(valor, (int, float)):
        raise ValueError("O valor da compra deve ser um número.")
    
    if valor < 0:
        raise ValueError("O valor da compra não pode ser negativo.")
    
    valor = int(valor)  # descarta os centavos 
    
    if redex and cartaox:
        pontos = valor * 3
    elif redex:
        pontos = valor * 1.5
    elif cartaox:
        pontos = valor
    else:
        pontos = 0

    return int(pontos)  # retorna um inteiro

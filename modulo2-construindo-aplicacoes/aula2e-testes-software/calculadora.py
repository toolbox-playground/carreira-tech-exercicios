def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def aplicar_desconto(preco, percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual deve estar entre 0 e 100")
    return preco * (1 - percentual / 100)


def calcular_total(preco, quantidade, desconto=0):
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa")
    subtotal = preco * quantidade
    return aplicar_desconto(subtotal, desconto)

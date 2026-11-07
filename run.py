from datetime import date


def calcular_idade(data_nascimento, hoje=None):
    if hoje is None:
        hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if hoje.month < data_nascimento.month:
        idade = idade - 1
    elif hoje.month == data_nascimento.month and hoje.day < data_nascimento.day:
        idade = idade - 1

    return idade


def dias_faltam(data_futura, hoje=None):
    if hoje is None:
        hoje = date.today()

    diferenca = data_futura - hoje
    return diferenca.days
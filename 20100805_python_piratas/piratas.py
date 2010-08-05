def divide_tesouro(tesouro, numero_piratas):
    if sum(tesouro.values()) < numero_piratas:
        return False

    valor_das_moedas = [quantidade * moeda for moeda, quantidade in tesouro.items()]
    total_das_moedas = sum(valor_das_moedas)

    if total_das_moedas % numero_piratas:
        return False

    return sum(valor_das_moedas) / numero_piratas

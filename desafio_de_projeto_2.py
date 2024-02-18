vitorias = 70
derrotas = 2
saldoVitorias = vitorias - derrotas

def classificacao(saldo):
    if saldo <= 10:
        rank = "Ferro"  
    elif saldo > 10 and saldo < 21:
        rank = "Bronze"  
    elif saldo > 20 and saldo < 51:
        rank = "Prata"
    elif saldo > 50 and saldo < 81:
        rank = "Ouro"
    elif saldo > 80 and saldo < 91:
        rank = "Diamante"
    elif saldo > 90 and saldo < 101:
        rank = "Lendário"
    elif saldo > 100:
        rank = "Imortal"

    return rank

nivel = classificacao(saldoVitorias)

print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}")

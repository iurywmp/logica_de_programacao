heroi = "Optimus"
pontos = 20000
xp = "nenhum"

if pontos <= 1000:
    xp = "Ferro"

elif pontos>= 1001 and pontos <= 2000:
    xp = "Bronze"

elif pontos>= 2001 and pontos <= 5000:
    xp = "Prata"

elif pontos>= 5001 and pontos <= 7000:
    xp = "Ouro"

elif pontos>= 7001 and pontos <= 8000:
    xp = "Platina"

elif pontos>= 8001 and pontos <= 9000:
    xp = "Ascendente"

elif pontos>= 9001 and pontos <= 10000:
    xp = "Imortal"

elif pontos>= 10001:
    xp = "Radiante"

print("O Herói de nome", heroi, "está no nível de", xp)
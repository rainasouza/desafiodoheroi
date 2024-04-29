
name = input("Digite o nome do seu herói: ")
experience = int(input("Digite a quantidade de XP, ou seja, a experiência do seu herói: "))

def determinar_nivel(experience):
    if experience < 1000:
        return "ferro"
    elif experience <= 2000:
        return "bronze"
    elif experience <= 5000:
        return "prata"
    elif experience <= 7000:
        return "ouro"
    elif experience <= 8000:
        return "platina"
    elif experience <= 9000:
        return "ascendente"
    elif experience <= 10000:
        return "imortal"
    else:
        return "radiante"
    
nivel = determinar_nivel(experience)
print(f"O Herói de nome {name} está no nível de {nivel}.")

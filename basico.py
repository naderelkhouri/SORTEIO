import random


def sorteio():

    acao = [
        "Beijo", "Cheiro", "Linguada",
        "Linguada lenta", "Tapa",
        "Assoprar", "Arranhar", "Dedada",
        "Só a cabecinha", "3 Bombadas Lentas", "3 Bombadas Rápidas"
    ]

    local = [
        "Boca", "Pepeca", "Pênis",
        "Atrás da orelha", "Pescoço", "Coxa",
        "Braço", "Nariz", "Orelha",
        "Bunda", "Ânus", "Peito",
        "Barriga"
    ]

    c = random.choice(acao)
    if c == "Só a cabecinha":
        d = ""
    elif c == "3 Bombadas Lentas":
        d = ""
    elif c == "3 Bombadas Rápidas":
        d = ""
    else:
        d = random.choice(local)

    print(f"{c} {d}")


if __name__ == "__main__":
    sorteio()

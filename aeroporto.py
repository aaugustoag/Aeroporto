from random import randint

pista1 = [[0,'D',0]]
pista2 = [[0,'D',0]]
pista3 = [[0,'D',0]]
aeroporto = [pista1, pista2, pista3]
id_aviao = 100000


def novas_decolagens(id_aviao, decolagens):
    n = 0
    n_aeronaves = randint(1,3)
    while n < n_aeronaves:
        decolagens.append([id_aviao, 'D', randint(1,20)])
        id_aviao += 1
        n += 1
    #print(decolagens)
    return decolagens

def novos_pousos (id_aviao, pousos):
    n = 0
    n_aeronaves = randint(1, 3)
    while n < n_aeronaves:
        pousos.append([id_aviao, 'P', randint(1,20)])
        id_aviao += 1
        n += 1
    #print(pousos)
    return pousos

def menor_prioridade(pista):
    menor_prioridade = 10000
    for i, aviao in enumerate(pista):
        if menor_prioridade > aviao[2] - i:
            menor_prioridade = aviao[2] - i
    return menor_prioridade

def define_decolagens (decolagens, aeroporto):
    for aviao in decolagens:
        p = 2;
        for i in range(3):
            if len(aeroporto[i]) == 0:
                aeroporto[i].append(aviao)
                p = i
                break
        if p == 2:
            if len(aeroporto[0]) < len(aeroporto[1]):
                if len(aeroporto[0]) < len(aeroporto[2]):
                    if menor_prioridade(aeroporto[0]) > 2:
                        p = 0
            elif len(aeroporto[1]) < len(aeroporto[2]):
                if menor_prioridade(aeroporto[1]) > 2:
                     p = 1
            else:
                aeroporto[2].append(aviao)
            if p < 2:
                aeroporto[p].insert(0, aviao)
            print("Aeronave " + str(aviao[0]) + ": Pista" + str(p+1) +" para decolar")
    return aeroporto

def define_pousos (pousos, aeroporto):
    for aviao in pousos:
        for i in range(3):
            if i < 2:
                if len(aeroporto[i]) <= len(aeroporto[i+1]):
                    if len(aeroporto[i]) == 0:
                        aeroporto[0].append(aviao)
                        print("Aeronave " + str(aviao[0]) + ": Pista1/" + str(j+1) + " com " + str(aviao[2]) + "L")
                    else:
                        if aviao[2] > aeroporto[i][-1][2]:
                            if aviao[2] == len(aeroporto[i])-1:
                                aeroporto[0].append(aviao)
                                print("Aeronave " + str(aviao[0]) + ": Pista1/" + str(j+1) + " com " + str(aviao[2]) + "L")
                        else:
                            for j, posicao in enumerate(aeroporto[i]):
                                if posicao[2] > aviao[2]:
                                    if menor_prioridade(aeroporto[i][j:]) > 2:
                                        aeroporto[i].insert(j, aviao)
                                        print("Aeronave " + str(aviao[0]) + ": Pista1/" + str(j+1) + " com " + str(aviao[2]) + "L")
                                    break
            else:
                if len(aeroporto[i]) == 0:
                    aeroporto[0].append(aviao)
                    print("Aeronave " + str(aviao[0]) + ": Pista1/" + str(j + 1) + " com " + str(aviao[2]) + "L")
                else:
                    for j, posicao in enumerate(aeroporto[2]):
                        if posicao[1] == 'P':
                            if posicao[2] > aviao[2]:
                                if menor_prioridade(aeroporto[2][j:]) > 2:
                                    aeroporto[1].insert(i, aviao)
                                    print("Aeronave " + str(aviao[0]) + ": Pista2/" + str(i + 1) + " com " + str(
                                        aviao[2]) + "L")
                                break
                        else:
                            aeroporto[1].insert(i, aviao)
                            print(
                                "Aeronave " + str(aviao[0]) + ": Pista2/" + str(i + 1) + " com " + str(aviao[2]) + "L")
                            break

    return aeroporto

def controle_de_trafego (aeroporto):
    for i in range(3):
        if len(aeroporto[i]) > 0:
            if i < 2:
                for aviao in aeroporto[i]:
                    if aviao[1] == 'P':
                        aviao[2] -= 1
                        if aviao[2] == 0:
                            print("**********EMERGENCIA**********")
                            print("Aeronave " + str(aviao[0]) + ": Pista" + str(i + 1) + " sem combustivel")
                            print("**********EMERGENCIA**********")
                        elif aviao[2] < 0:
                            print("**********BOOM!!!**********")
                            print("Aeronave " + str(aviao[0]) + ": Pista" + str(i + 1) + " com pane seca")
                            print("*****************************************")
                            exit()
            if aeroporto[i][0][1] == 'D':
                print("Aeronave " + str(aeroporto[i][0][0]) + ": decolou da pista" + str(i+1))
            else:
                print("Aeronave " + str(aeroporto[i][0][0]) + ": pousou na pista" + str(i+1))
            aeroporto[i].remove(aeroporto[i][0])
    return aeroporto

tempo = 30

for i in range(tempo):
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("Tempo " + str(i+1))
    pousos = []
    decolagens = []
    novos_pousos(id_aviao, pousos)
    print("Pousos" + str(i+1) + ": "+ str(pousos))
    id_aviao = pousos[-1][0] + 1
    novas_decolagens(id_aviao, decolagens)
    print("Decolagens" + str(i+1) + ": "+ str(decolagens))
    id_aviao = decolagens[-1][0] + 1
    print("---------------")
    aeroporto = define_pousos(pousos, aeroporto)
    aeroporto = define_decolagens(decolagens, aeroporto)
    print("---------------")
    aeroporto = controle_de_trafego(aeroporto)
    print("---------------")
    print("Pista 1: " + str(pista1))
    print("Pista 2: " + str(pista2))
    print("Pista 3: " + str(pista3))
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
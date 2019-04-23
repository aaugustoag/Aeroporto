from random import randint

pista1 = [0,'D',0]
pista2 = [0,'D',0]
pista3 = [0,'D',0]
aeroporto = [pista1, pista2, pista3]
fila_pouso = [[[0,'P',0]],[[0,'P',0]],[[0,'P',0]],[[0,'P',0]]]
fila_decolagem = [[[0,'D',0]],[[0,'D',0]],[[0,'D',0]]]
id_aviao = 100000


def novas_decolagens(id_aviao, decolagens):
    n = 0
    n_aeronaves = randint(0,3)
    while n < n_aeronaves:
        decolagens.append([id_aviao, 'D', randint(1,20)])
        id_aviao += 1
        n += 1
    #print(decolagens)
    return decolagens

def novos_pousos (id_aviao, pousos):
    n = 0
    n_aeronaves = randint(0, 3)
    while n < n_aeronaves:
        pousos.append([id_aviao, 'P', randint(1,20)])
        id_aviao += 1
        n += 1
    #print(pousos)
    return pousos

def menor_prioridade(fila):
    menor_prioridade = 10000
    for i, aviao in enumerate(fila):
        if menor_prioridade > aviao[2] - i:
            menor_prioridade = aviao[2] - i
    return menor_prioridade

def define_decolagens (decolagens, fila_decolagem):
    for aviao in decolagens:
        if len(fila_decolagem[0]) < len(fila_decolagem[1]):
            if len(fila_decolagem[0]) < len(fila_decolagem[2]):
                p = 0
        elif len(fila_decolagem[1]) < len(fila_decolagem[2]):
            p = 1
        else:
            p = 2
        fila_decolagem[p].append(aviao)
        print("Aeronave " + str(aviao[0]) + ": Pista" + str(p+1) +" para decolar")
    return fila_decolagem

def define_pousos (pousos, fila_pouso):
    for aviao in pousos:
        if len(fila_pouso[0]) < len(fila_pouso[1]):
            if len(fila_pouso[0]) < len(fila_pouso[2]):
                if len(fila_pouso[0]) < len(fila_pouso[3]):
                    p = 0
        elif len(fila_pouso[1]) < len(fila_pouso[2]):
            if len(fila_pouso[1]) < len(fila_pouso[3]):
                p = 1
        elif len(fila_pouso[2]) < len(fila_pouso[3]):
            p = 2
        else:
            p = 3
        fila_pouso[p].append(aviao)
        print("Aeronave " + str(aviao[0]) + ": Pista" + str(int(p/2)+1) + " com " + str(aviao[2]) + "L")
    return fila_pouso

def controle_de_trafego (aeroporto, fila_pouso, fila_decolagem):
    p = 2
    for i in range(4):
        if p < 0:
            break
        for aeronave in fila_pouso[i]:
            if p < 0:
                break
            if aeronave < 2:
                aeroporto[p] = aeronave
                fila_pouso[i].remove(aeronave)
                p -= 1

        if p < 3:
            elif fila_pouso[0][2] < fila_pouso[1][2]:
                aeroporto[0] = fila_pouso[0][0]
                fila_pouso[0].remove(fila_pouso[0][0])
            else:
                aeroporto[0] = fila_pouso[1][0]
                fila_pouso[1].remove(fila_pouso[1][0])
        else:
            aeroporto[0] = fila_decolagem[0][0]
            fila_decolagem[0].remove(fila_decolagem[0][0])
            break
    if menor_prioridade(fila_pouso[2]) < 2:
        if menor_prioridade(fila_pouso[3]) < 2:
            if fila_pouso[2][2] < fila_pouso[3][2]:
                aeroporto[1] = fila_pouso[2][0]
                fila_pouso[2].remove(fila_pouso[2][0])
            else:
                aeroporto[1] = fila_pouso[3][0]
                fila_pouso[3].remove(fila_pouso[3][0])
        else:
            aeroporto[0] = fila_decolagem[0][0]
            fila_decolagem[0].remove(fila_decolagem[0][0])


    for i in range(3):
        if len(aeroporto[i]) > 0:
            if i < 2:
                for aviao in aeroporto[i]:
                    if aviao[1] == 'P':
                        aviao[2] -= 1
                        if aviao[2] == 0:
                            print("******************EMERGENCIA******************")
                            print("Aeronave " + str(aviao[0]) + ": Pista" + str(i + 1) + " sem combustivel")
                            print("******************EMERGENCIA******************")
                        elif aviao[2] < 0:
                            print("********************BOOM!!!********************")
                            print("Aeronave " + str(aviao[0]) + ": Pista" + str(i + 1) + " com pane seca")
                            print("***********************************************")
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
    if len(pousos) > 0:
        id_aviao = pousos[-1][0] + 1
    novas_decolagens(id_aviao, decolagens)
    if len(decolagens) > 0:
        id_aviao = decolagens[-1][0] + 1
    print("---------------")
    fila_pouso = define_pousos(pousos, fila_pouso)
    print("Pousos1/1" + ": "+ str(fila_pouso[0]))
    print("Pousos1/2" + ": "+ str(fila_pouso[1]))
    print("Pousos2/1" + ": "+ str(fila_pouso[2]))
    print("Pousos2/2" + ": "+ str(fila_pouso[3]))
    fila_decolagem = define_decolagens(decolagens, fila_decolagem)
    print("Decolagens" + str(i+1) + ": "+ str(fila_decolagem[0]))
    print("Decolagens" + str(i+1) + ": "+ str(fila_decolagem[1]))
    print("Decolagens" + str(i+1) + ": "+ str(fila_decolagem[2]))
    print("---------------")
    '''
    aeroporto = controle_de_trafego(aeroporto)
    print("---------------")
    print("Pista 1: " + str(pista1))
    print("Pista 2: " + str(pista2))
    print("Pista 3: " + str(pista3))
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    '''
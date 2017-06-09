print('>>> FIFO ou SJF <<<')
alg = input('Digite qual o tipo do algoritmo: ')  # Usuário digitarar se é FIFO ou SJF
# p = PROCESSO#
print('Programa testado apenas com  os processoas 23,10,9,5,3 e 2.')
print('A fila está de acordo com o exemplo do slid.A,C,B,D,E e F')

if alg == 'FIFO':
    p_a = int(input('Digite o tempo do processo A: '))  # 23
    p_c = int(input('Digite o tempo do processo C: '))  # 10
    p_b = int(input('Digite o tempo do processo B: '))  # 9
    p_d = int(input('Digite o tempo do processo D: '))  # 5
    p_e = int(input('Digite o tempo do processo E: '))  # 3
    p_f = int(input('Digite o tempo do processo F: '))  # 2
    print('________________________________________________________')
    tur_p_a = p_a
    tem_p_a = 0
    print('|processo A| Tempo de Turnaround {}| Tempo de Espera {} |'.format(tur_p_a,tem_p_a))
    tur_p_c = p_c + p_a
    tem_p_c = tem_p_a + p_a
    print('|processo C| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_c,tem_p_c))
    tur_p_b = p_c + p_a + p_b
    tem_p_b = tem_p_c + p_c
    print('|processo B| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_b,tem_p_b))
    tur_p_d = p_c + p_a + p_b + p_d
    tem_p_d = tem_p_b + p_b
    print('|processo D| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_d,tem_p_d))
    tur_p_e = p_c + p_a + p_b + p_d + p_e
    tem_p_e = tem_p_d + p_d
    print('|processo E| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_e,tem_p_e))
    tur_p_f = p_c + p_a + p_b + p_d + p_e + p_f
    tem_p_f = tem_p_e + p_e
    print('|processo F| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_f,tem_p_f))
    print('_______________________________________________________')
    tempo_medio = ((tem_p_a + tem_p_c) + (tem_p_b + tem_p_d) + (tem_p_e + tem_p_f)) / 6

    print('>> O tempo médio foi de {:.1f} s <<.'.format(tempo_medio))
    input()

elif alg == 'SJF':
    pilha = [0, 0, 0, 0, 0, 0]
    pilha[0] = int(input('Digite o tempo do processo A: '))
    pilha[1] = int(input('Digite o tempo do processo C: '))
    pilha[2] = int(input('Digite o tempo do processo B: '))
    pilha[3] = int(input('Digite o tempo do processo D: '))
    pilha[4] = int(input('Digite o tempo do processo E: '))
    pilha[5] = int(input('Digite o tempo do processo F: '))

    pilha.sort()  # Coloca em ordem
    print(pilha)

    print('________________________________________________________')
    tur_p_a = pilha[0] + pilha[1] + pilha[2] + pilha[3] + pilha[4] + pilha[5]
    tem_p_a = tur_p_a - pilha[5]
    print('|processo A| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_a,tem_p_a))
    tur_p_c = pilha[0] + pilha[1] + pilha[2] + pilha[3] + pilha[4]
    tem_p_c = tur_p_c - pilha[4]
    print('|processo C| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_c,tem_p_c))
    tur_p_b = pilha[0] + pilha[1] + pilha[2] + pilha[3]
    tem_p_b = tur_p_b - pilha[3]
    print('|processo B| Tempo de Turnaround {}| Tempo de Espera {}|'.format(tur_p_b,tem_p_b))
    tur_p_d = pilha[0] + pilha[1] + pilha[2]
    tem_p_d = tur_p_d - pilha[2]
    print('|processo D| Tempo de Turnaround {}| Tempo de Espera  {}|'.format(tur_p_d,tem_p_d))
    tur_p_e = pilha[0] + pilha[1]
    tem_p_e = tur_p_e - pilha[1]
    print('|processo E| Tempo de Turnaround  {}| Tempo de Espera  {}|'.format(tur_p_e,tem_p_e))
    tur_p_f = pilha[0]
    tem_p_f = 0
    print('|processo F| Tempo de Turnaround  {}| Tempo de Espera  {}|'.format(tur_p_f,tem_p_f))

    print('________________________________________________________')
    tempo_medio = (tem_p_a + tem_p_c + tem_p_b + tem_p_d + tem_p_e + tem_p_f) / 6 # PEGA * OS TEMPOS DOS PROCESSOS E DIVIDE PELA QUANT DE PROCESSOS.
    print('>> O tempo médio foi de {:.1f} s <<.'.format(tempo_medio))
    input()

else:
    print('Tipo de escalonamento não disponivel.')


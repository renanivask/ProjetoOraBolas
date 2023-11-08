import math
import matplotlib.pyplot as plt

def info_arquivo(file_path):
    valores_de_x = []
    valores_de_y = []
    valores_do_tempo = []

    with open(file_path, 'r') as file:
        next(file)

        for linha in file:
            linha = linha.strip().replace(',', '.')
            tempo, x, y = map(float, linha.split('\t'))
            valores_do_tempo.append(tempo)
            valores_de_x.append(x)
            valores_de_y.append(y)

    return valores_do_tempo, valores_de_x, valores_de_y

tempos, bola_x, bola_y = info_arquivo("bola.txt")

aceleracao_r = 2.8
raio_r = 0.09
raio_b = 0.0105

S0x = float(input("Digite a posição inicial da bola em X: "))
S0y = float(input("Digite a posição inicial da bola em Y: "))

raio_interceptacao = raio_b + raio_r

tempo_interceptacao = 99999
x_bola_imediato = 0.0
y_bola_imediato = 0.0
distancia_total = 0.0

# calcular tempo_interceptacao
for i in range(len(bola_x)):
    x_bola_imediato = bola_x[i]
    y_bola_imediato = bola_y[i]
    tempo_max_interceptacao = tempos[i]
    distancia = (((x_bola_imediato - S0x)**2 + (y_bola_imediato - S0y)**2)**0.5) + raio_interceptacao
    t = (distancia/(0.5*aceleracao_r))**0.5
    if t <= tempo_max_interceptacao:
        tempo_interceptacao = t
        distancia_total = distancia
        print("Tempo necessário para a interceptação: ", tempo_interceptacao)
        print("Ponto x de interceptação: ", x_bola_imediato,
              "\nPonto y de interceptação: ", y_bola_imediato)
        print("Tempo até interceptação: ", tempo_max_interceptacao)
        break

tempo_agora = 0.0
sx_imediato = S0x
sy_imediato = S0y
aceleracao_x = (x_bola_imediato - sx_imediato)/distancia_total * aceleracao_r
aceleracao_y = (y_bola_imediato - sy_imediato)/distancia_total * aceleracao_r
poiscao_x = []
poiscao_y = []

# Posicoes pro grafico do robo
while True:
    if tempo_agora >= tempo_interceptacao:
        break
    x_agora = S0x + (aceleracao_x * (tempo_agora**2))/2
    y_agora = S0y + (aceleracao_y * (tempo_agora**2))/2
    tempo_agora += 0.001
    poiscao_x.append(x_agora)
    poiscao_y.append(y_agora)

# Crie listas vazias para armazenar as grandezas de interesse
posicao_x_r = []
posicao_y_r = []
posicao_x_b = []
posicao_y_b = []
velocidade_x_r_lista = []
velocidade_y_r_lista = []
velocidade_x_b_lista = []
velocidade_y_b_lista = []
acel_x_r_lista = []
acel_y_r_lista = []
acel_x_b_lista = []
acel_y_b_lista = []
distancia_relativa_lista = []

# Posicoes, velocidades, acelerações e distância
for tempo in tempos:
    x_imediato_r = sx_imediato + (aceleracao_x * (tempo**2))/2
    y_imediato_r = sy_imediato + (aceleracao_y * (tempo**2))/2
    x_imediato_b = x_bola_imediato
    y_imediato_b = y_bola_imediato
    velocidade_x_r = aceleracao_x * tempo
    velocidade_y_r = aceleracao_y * tempo
    velocidade_x_b = 0.0
    velocidade_y_b = 0.0
    acel_x_r = aceleracao_x
    acel_y_r = aceleracao_y
    acel_x_b = 0.0
    acel_y_b = 0.0
    distancia_relativa = ((x_imediato_r - x_imediato_b)**2 + (y_imediato_r - y_imediato_b)**2)**0.5

    posicao_x_r.append(x_imediato_r)
    posicao_y_r.append(y_imediato_r)
    posicao_x_b.append(x_imediato_b)
    posicao_y_b.append(y_imediato_b)

    velocidade_x_r_lista.append(velocidade_x_r)
    velocidade_y_r_lista.append(velocidade_y_r)
    velocidade_x_b_lista.append(velocidade_x_b)
    velocidade_y_b_lista.append(velocidade_y_b)

    acel_x_r_lista.append(acel_x_r)
    acel_y_r_lista.append(acel_y_r)
    acel_x_b_lista.append(acel_x_b)
    acel_y_b_lista.append(acel_y_b)

    distancia_relativa_lista.append(distancia_relativa)

# Menu interativo
while True:
    print("\nEscolha o tipo de gráfico:")
    print("1. Gráfico das trajetórias da bola e do robô em um plano xy, até o ponto de interceptação")
    print("2. Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡")
    print("3. Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡")
    print("4. Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡")
    print("5. Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        plt.figure(figsize=(8, 6))
        plt.plot(bola_x, bola_y, color="blueviolet", marker=",", label="Trajetória da Bola")
        plt.plot(posicao_x_r, posicao_y_r, color="darkcyan", marker=",", label="Trajetória do Robô")
        plt.xlabel("Posição X")
        plt.ylabel("Posição Y")
        plt.title("Trajetórias da Bola e do Robô")
        plt.legend()
        plt.xlim(0, 9.0)
        plt.ylim(0, 6.0)
        plt.grid(True)
        plt.show()
  
    if escolha == "2":
        # Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, bola_x, color="blueviolet", marker=",", label="Posição Bola X")
        plt.plot(tempos, posicao_x_r, color="darkcyan", marker=",", label="Posição Robô X")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição X")
        plt.title("Coordenadas de x da Posição da Bola e do Robô")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, bola_y, color="blueviolet", marker=",", label="Posição Bola Y")
        plt.plot(tempos, posicao_y_r, color="darkcyan", marker=",", label="Posição Robô Y")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição Y")
        plt.title("Coordenadas de y da Posição da Bola e do Robô")
        plt.legend()

        plt.show()

    elif escolha == "3":
        # Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, velocidade_x_r_lista, color="darkcyan", marker=",", label="Velocidade X Robô")
        plt.plot(tempos, velocidade_x_b_lista, color="blueviolet", marker=",", label="Velocidade X Bola")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade X")
        plt.title("Componente vx da Posição da Bola e do Robô")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, velocidade_y_r_lista, color="darkcyan", marker=",", label="Velocidade Y Robô")
        plt.plot(tempos, velocidade_y_b_lista, color="blueviolet", marker=",", label="Velocidade Y Bola")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade Y")
        plt.title("Componente vy da Posição da Bola e do Robô")
        plt.legend()

        plt.tight_layout()
        plt.show()

    elif escolha == "4":
        # Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, acel_x_r_lista, color="darkcyan", label="Aceleração X Robô")
        plt.plot(tempos, acel_x_b_lista, color="blueviolet", label="Aceleração X Bola")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração X")
        plt.title("Componente ax da Posição da Bola e do Robô")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, acel_y_r_lista, color="darkcyan", label="Aceleração Y Robô")
        plt.plot(tempos, acel_y_b_lista, color="blueviolet", label="Aceleração Y Bola")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração Y")
        plt.title("Componente ay da Posição da Bola e do Robô")
        plt.legend()

        plt.tight_layout()
        plt.show()


    elif escolha == "5":
        # Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, distancia_relativa_lista, color="darkcyan", marker=",", label="Distância Relativa")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Distância Relativa")
        plt.title("Distância relativa d entre o robô e a bola como função do tempo")
        plt.legend()

        plt.show()

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")

import math
import matplotlib.pyplot as plt

def read_data_from_file(file_path):
    x_values = []
    y_values = []
    time_values = []

    with open(file_path, 'r') as file:
        next(file)

        for line in file:
            line = line.strip().replace(',', '.')
            time, x, y = map(float, line.split('\t'))
            time_values.append(time)
            x_values.append(x)
            y_values.append(y)

    return time_values, x_values, y_values

tempos, bola_x, bola_y = read_data_from_file("bola.txt")

acel_robo = 2.8
raio_robo = 0.09
raio_bola = 0.0105

S0x = float(input("Digite o espaço inicial de x: "))
S0y = float(input("Digite o espaço inicial de y: "))

raio_interceptacao = raio_bola + raio_robo

dt = 99999
bola_x_agora = 0.0
bola_y_agora = 0.0
dist_total = 0.0

# calcula o dt
for i in range(len(bola_x)):
    bola_x_agora = bola_x[i]
    bola_y_agora = bola_y[i]
    tmax = tempos[i]
    distancia = (((bola_x_agora - S0x)**2 + (bola_y_agora - S0y)**2)**0.5) + raio_interceptacao
    t = (distancia/(0.5*acel_robo))**0.5
    if t <= tmax:
        dt = t
        dist_total = distancia
        print(dt)
        print(bola_x_agora,bola_y_agora)
        print(tmax)
        break

tempo_agora = 0.0
sx_agora = S0x
sy_agora = S0y
acel_x = (bola_x_agora - sx_agora)/dist_total * acel_robo
acel_y = (bola_y_agora - sy_agora)/dist_total * acel_robo
pos_x = []
pos_y = []

# Posições para o gráfico do robô
while True:
    if tempo_agora >= dt:
        break
    x_agora = S0x + (acel_x * (tempo_agora**2))/2
    y_agora = S0y + (acel_y * (tempo_agora**2))/2
    tempo_agora += 0.001
    pos_x.append(x_agora)
    pos_y.append(y_agora)

# Cria listas vazias para armazenar as grandezas de interesse
pos_x_robo = []
pos_y_robo = []
pos_x_bola = []
pos_y_bola = []
vel_x_robo_list = []
vel_y_robo_list = []
vel_x_bola_list = []
vel_y_bola_list = []
acel_x_robo_list = []
acel_y_robo_list = []
acel_x_bola_list = []
acel_y_bola_list = []
dist_rel_list = []

# Posições, velocidades, acelerações e distância
for tempo in tempos:
    x_agora_robo = sx_agora + (acel_x * (tempo**2))/2
    y_agora_robo = sy_agora + (acel_y * (tempo**2))/2
    x_agora_bola = bola_x_agora
    y_agora_bola = bola_y_agora
    vel_x_robo = acel_x * tempo
    vel_y_robo = acel_y * tempo
    vel_x_bola = 0.0
    vel_y_bola = 0.0
    acel_x_robo = acel_x
    acel_y_robo = acel_y
    acel_x_bola = 0.0
    acel_y_bola = 0.0
    dist_rel = ((x_agora_robo - x_agora_bola)**2 + (y_agora_robo - y_agora_bola)**2)**0.5

    pos_x_robo.append(x_agora_robo)
    pos_y_robo.append(y_agora_robo)
    pos_x_bola.append(x_agora_bola)
    pos_y_bola.append(y_agora_bola)

    vel_x_robo_list.append(vel_x_robo)
    vel_y_robo_list.append(vel_y_robo)
    vel_x_bola_list.append(vel_x_bola)
    vel_y_bola_list.append(vel_y_bola)

    acel_x_robo_list.append(acel_x_robo)
    acel_y_robo_list.append(acel_y_robo)
    acel_x_bola_list.append(acel_x_bola)
    acel_y_bola_list.append(acel_y_bola)

    dist_rel_list.append(dist_rel)

# Menu interativo
while True:
    print("\nEscolha o tipo de gráfico:")
    print("1. Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação")
    print("2. Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡")
    print("3. Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡")
    print("4. Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡")
    print("5. Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        # Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡
        plt.figure(figsize=(8, 6))
        plt.plot(bola_x, bola_y, color="red", marker="o", label="Trajetória da Bola")
        plt.plot(pos_x_robo, pos_y_robo, color="blue", marker="o", label="Trajetória do Robô")
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
        plt.plot(tempos, bola_x, color="red", marker="o", label="Pos Bola X")
        plt.plot(tempos, pos_x_robo, color="blue", marker="o", label="Pos Robô X")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição X")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, bola_y, color="red", marker="o", label="Pos Bola Y")
        plt.plot(tempos, pos_y_robo, color="blue", marker="o", label="Pos Robô Y")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição Y")
        plt.legend()

        plt.show()

    elif escolha == "3":
        # Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, vel_x_robo_list, color="blue", marker="o", label="Velocidade X Robô")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade X")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, vel_y_robo_list, color="blue", marker="o", label="Velocidade Y Robô")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade Y")
        plt.legend()

        plt.tight_layout()
        plt.show()

    elif escolha == "4":
        # Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, acel_x_robo_list, color="blue", label="Aceleração X Robô")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração X")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, acel_y_robo_list, color="blue", label="Aceleração Y Robô")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração Y")
        plt.legend()

        plt.tight_layout()
        plt.show()

    elif escolha == "5":
        # Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.plot(tempos, dist_rel_list, color="blue", marker="o", label="Distância Relativa")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Distância Relativa")
        plt.legend()

        plt.show()

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")

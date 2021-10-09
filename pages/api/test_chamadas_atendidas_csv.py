import csv, urllib.request

url = 'https://raw.githubusercontent.com/msestrem/api-teste-nextjs/main/chamadas_atendidas.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)


for row in cr:
    # print(lines[0].count(','))
    # if (lines[0].count(',') < 2):
    #   print('Não tem nota fiscal: {0}'.format(lines))
    #    continue
    if 'Data' in row[0].split(',', 1)[0]:
        continue
    data = row[0].split(',', 1)[0]
    fila = row[1].split(',', 2)[0]
    atendente = row[2].split(',', 3)[0]
    tempo_de_espera = row[3].split(',', 4)[0]
    duracao = row[4].split(',', 5)[0]
    numero = row[5].split(',', 6)[0]
    print('Data: '+data)
    print('Fila: '+fila)
    print('Atendente: '+atendente)
    print('Tempo de Espera: '+tempo_de_espera)
    print('Duração: '+duracao)
    print('Número: '+numero)
    print()
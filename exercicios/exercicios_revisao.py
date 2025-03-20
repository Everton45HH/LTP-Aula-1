import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
    mensagem = f"Boa tarde, {nome}. Seja bem vindo!"
    return mensagem

# 2. Faça uma função que peça o raio de um círculo e retorne sua área.
def area_circulo(raio):

    area = math.pi * raio ** 2

    return area


# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius(f):

    c  = 5 * ((f-32) / 9)

    return c

# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# Alexandre Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como 
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
def calculo_multa(peixada):
    
    excesso = peixada - 50

    multa = 4 * excesso

    if excesso > 0:
        # mensagem = f'Excesso de peso: {excesso} kg. \nMulta a pagar: R$ {multa}.00.'
        mensagem = 'Excesso de peso: 10 kg.\nMulta a pagar: R$ 40.00.'
        return mensagem

    else:
        mensagem = 'Peso dentro do limite. Nenhuma multa aplicada.'
        return mensagem



# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga no cálculo de litros necessários para cobrir
# a área a ser pintada e sempre arredonde os valores para cima, 
# isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
# 
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00
def calcular_tinta(area):
    pass

# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero(x,y):
    if x>y:
        return x
    else:
        return y

# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return("Vogal")
    else:
        return("Consoante")
# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(x,y,z):

    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    else:
        return z
# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno(letra):
    if letra == 'M':
        mensagem = "Bom Dia!"
    elif letra == 'V':
        mensagem = "Boa Tarde!"
    elif letra == 'N':
        mensagem = "Boa Noite!"
    else:
        mensagem = "Valor Inválido!"
    return mensagem


# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e e retornará quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico(saque):

    valor = saque
    notas_cem , notas_dez , notas_cinco , notas_um = 0 , 0 , 0 , 0 

    while valor >= 100:
        notas_cem +=1
        valor = valor - 100

    while valor >= 10:
        notas_dez +=1
        valor = valor - 10

    while valor >= 5:
        notas_cinco +=1
        valor = valor - 5
    
    while valor >= 1:
        notas_um +=1
        valor = valor - 1
    

    notas = [100,10,5,1]
    notas_quantidades = [notas_cem,notas_dez,notas_cinco,notas_um]
    esperado = ''
    for i in range(len(notas)):
        esperado += f'{notas_quantidades[i]} nota(s) de R$ {notas[i]}\n'
    return 'Notas fornecidas:\n' + esperado
print(caixa_eletronico(256))
# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def classificar_participacao(respostas):

    culpado = 0
    for x in range(len(respostas)):
        if respostas[x] == 's':
            culpado+=1
        else:
            pass

    if culpado == 5:
        return "Assassino"
    
    elif  3 <= culpado and culpado <= 4:
        return "Cumplice"
    
    if culpado>=2:
        return "Cúmplice"
    
    else:
        return "Suspeita"

# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo, quantidade, pagamento_cartao):
    if tipo == "File Duplo":
        preco = 4.90 if quantidade <= 5 else 5.80
    elif tipo == "Alcatra":
        preco = 5.90 if quantidade <= 5 else 6.80
    elif tipo == "Picanha":
        preco = 6.90 if quantidade <= 5 else 7.80
    else:
        return "Tipo de carne inválido"

    preco_total = preco * quantidade
    desconto = 0

    if pagamento_cartao:
        desconto = preco_total * 0.05

    valor_a_pagar = preco_total - desconto

    cupom_fiscal = (
        f"Tipo de carne: {tipo}\n"
        f"Quantidade: {quantidade} Kg\n"
        f"Preço total: R$ {preco_total}\n"
        f"Tipo de pagamento: {'Cartão Tabajara' if pagamento_cartao else 'Outro'}\n"
        f"Valor do desconto: R$ {desconto}\n"
        f"Valor a pagar: R$ {valor_a_pagar}"
    )

    return cupom_fiscal

# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
def potencia(a,b):

    return a ** b

# 15. Faça um Programa que retorne o menor, maior e a soma de um *args de números.
def estatisticas_numeros(*args):
    lista = []
    for i in args:
        if isinstance(i, list):  # Se for uma lista, adiciona os elementos
            lista.extend(i)
        else:  # Se for um número, adiciona normalmente
            lista.append(i)
    
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    
    return menor, maior, soma


estatisticas_numeros(3,7,5)
# 16. Faça uma função que valide se uma nota está entre 0 e 10.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Exemplos de saídas para as entradas -1 e 5.5 respectivamente:
# Erro: A nota deve estar entre 0 e 10. Tente novamente.
# Nota válida: 5.5

def validar_nota():
    while True:
        nota = input("Digite uma nota entre 0 e 10: ")
        if nota.replace('.', '', 1).isdigit():
            nota = float(nota)
            if 0 <= nota <= 10:
                return f"Nota válida: {nota:.2f}"
        print("Erro: A nota deve ser um número entre 0 e 10. Tente novamente")

# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():


        usuario = input("Digite seu usuario: ")
        senha = input("Digite sua senha: ")

        while usuario == senha:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
            usuario = input("Digite seu usuario: ")

        return("Usuário e senha cadastrados com sucesso!")

# 18. Faça um Programa que calcule a média aritmética de um *args de N notas.
def media_notas(nota):
    soma = 0
    for i in range(len(nota)):
        soma += int(nota[i])
    return soma / len(nota)

# 19. Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
def calcular_serie(n):
    soma = 0

    for i in range(0,n + 1):

        res = n / (n*2 - 1)

        soma += res

    return soma

# 20. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#  A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: João Silva
# Nota: 7.9
# Nota: 8.5
# Nota: 9.4
# Nota: 7.0
# Nota: 8.8
# Nota: 9.8
# Nota: 7.9

# Resultado final:
# Atleta: João Silva
# Melhor nota: 9.8
# Pior nota: 7.0
# Média: 8.50
def calcular_media_ginastica(nome,*args):
    melhor = 0
    pior = 1000000
    soma = 0

    for i in range(len(args)):
        soma += args[i]
        if args[i] > melhor :
            melhor = args[i]

        elif args[i] < pior:
            pior = args[i]
        
    return nome,melhor,pior,soma/len(args)

# 21. Faça um Programa que desenhe uma pirâmide alinhada à esquerda.
def piramide_esquerda(x):
    piramide = ''
    for i in range(1, x + 1):  # Começar de 1 e ir até x
        linha = '#' * i  # Cria a linha com i asteriscos
        piramide += linha + '\n'
    return piramide
        

# 22. Faça um Programa que desenhe uma pirâmide alinhada à direita.
def piramide_direita(altura):
    piramide = ''
    for i in range(1, altura + 1):
        espacos = ' ' * (altura - i)
        estrelas = '#' * i
        piramide += espacos + estrelas + '\n'

    return piramide

# 23. Faça um Programa que desenhe duas pirâmides lado a lado.
def piramides_lado_a_lado():
    pass

# 24. Faça um Programa que calcule o troco com a menor quantidade de moedas possível.
def calcular_troco():
    pass

# 25. Faça um Programa que valide um número de cartão de crédito usando o algoritmo de Luhn.
def validar_cartao():
    pass

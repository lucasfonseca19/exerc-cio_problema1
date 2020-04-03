#Importando biblioteca para o sorteio randômico de dados
import random
#Declarando lista de 1 a 6 representando os dados
dado1=[1,2,3,4,5,6]
dado2=[1,2,3,4,5,6]
#Estabelecendo o valor inicial de fichas para o jogador
fichas=100
#Declarando contadores utilizados ao longo do código
n=1
z=0
point=0
#Declarando variáveis utilizadas para armazenar a quantidade de fichas a serem apostadas em cada jogo
apostap=0
apostaf=0
apostat=0
apostaa=0
#Função que pergunta se o jogador que apostar ou não
def apostar():
    resp=input("\nVocê gostaria de apostar nessa rodada ou sair do jogo?\nDigite'apostar'ou'sair':\n")
    if (resp =='apostar'):
        return True
    else:
        return False
#Função que seleciona randômicamente valores pros dados e soma os resultado
def sorteio():
    x=random.choice(dado1)
    y=random.choice(dado2)
    resultado=x+y
    return resultado
#funções para modos de jogo
# * Uso de 'global' em fichas para que qualquer jogo altere a quantidade de fichas do usuário
# * Uso de 'global'em z para que um mesmo sorteio seja usado em mais de um jogo
# * Uso de 'global'em aposta(inicial do modo) para que qualquer aposta seja acessada facilmente pelo escopo global
def plb():
    global fichas 
    global z
    global apostap
    print("o número sorteado é:",z)
    if(z== 7 or z== 11):
        fichas=fichas+apostap 
        print("Agora você tem o total de: {} fichas".format(fichas))
    elif(z== 2 or z== 3 or z== 12):
        fichas=fichas-apostap
        print("Agora você tem o total de: {} fichas".format(fichas))
    elif(z== 4 or z== 5 or z== 6 or z== 8 or z== 9 or z== 10):   
        #Função para ser usado a frente com o while e ficar no modo point até atingir um veredito
        def loop_point():
            w=sorteio()
            global n
            global fichas
            print("\nAgora você se encontra na fase point referente ao modo plb pela {}° vez\n".format(n))
            print("O valor {} retirado no primeiro sorteio é seu point".format(z))
            print("O novo valor sorteado é",w)
            n=n+1
            
            if(w==z):
                fichas=fichas+apostap
                print("agora você possui{}fichas",format(fichas))
                return True
            elif(w==7):
                fichas=fichas-apostap
                print("Você perdeu tudo!!!")
                print("agora você possui{}fichas",format(fichas))
                return True
            else:
                return False
        while(loop_point()!=True):
            loop_point()
def field():
    global fichas
    global z
    global apostaf
    print("O número sorteado é:",z)
    if(z==5 or z==6 or z==7 or z==8):
        fichas=fichas-apostaf
        print('Você perdeu tudo !!!')
        print("Agora você tem o total de: {} fichas".format(fichas))
    elif(z==3 or z==4 or z==9 or z==10 or z==11):
        fichas=fichas
        print("Você contínua com o total de: {} fichas".format(fichas))
    elif(z==2):
        fichas=fichas+2*apostaf
        print("Agora você tem o total de: {} fichas ".format(fichas))
    else:
        fichas=fichas+3*apostaf
        print("Agora você tem o total de: {} fichas".format(fichas))
def anycraps():
    global fichas
    global z
    global apostaa
    print("o número sorteado é:",z)
    if(z==2 or z==3 or z==12):
        fichas=fichas+7*apostaa
        print("Agora você tem o total de: {} fichas".format(fichas))
    else:
        fichas=fichas-apostaa
        print("Agora você tem o total de: {} fichas".format(fichas))   
def twelve():
    global fichas
    global z
    global apostat
    print("o número sorteado é:",z)
    if(z==12):
        fichas=fichas+30*apostat
        print("Agora você tem o total de: {} fichas".format(fichas))
    else:
        fichas=fichas-apostat
        print("Agora você tem o total de: {} fichas".format(fichas))
#Função para armazenamento de tipos de apostas e os valores apostados até o usuário disser que acaabou
def apostas():
    #lista 'tipos'criada para armazenar modos selecionados
    tipos=[]
    while True:
        global z
        z=sorteio()
        
        tipo=input("Você se encontra na fase Come Out\n \nQuais tipos de aposta você gostaria de fazer?\n \n Digite 'plb' e/ou 'field' e/ou'anycraps' e/ou'twelve' separado por virgulas\nQuando terminar de escolher digite 'acabei' ")
        if (tipo =='acabei'):
            break
        #Armazena modos selecionados em uma na lista tipos
        tipos.append(tipo)
    #Percorre a lista criada anteriormente em busca dos modos de jogo inseridos e de acordo com o que encontar pergunta de quanto será a aposta
    for word in tipos:
        global apostaa,apostaf,apostap,apostat
        if word=='plb':
            apostap=int(input("Quantas fichas gostaria de jogar no PLB? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='field':
            apostaf=int(input("Quantas fichas gostaria de jogar no FIELD? lembrando que você só pode jogar um número inteiro de fichas"))   
        elif word=='anycraps':
            apostaa=int(input("Quantas fichas gostaria de jogar no ANYCRAPS? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='twelve':
            apostat=int(input("Quantas fichas gostaria de jogar no TWELVE? lembrando que você só pode jogar um número inteiro de fichas"))   
        '''Percorre novamente a lista, agora para executar a função de cada jogo'''  
    for word in tipos:
        if word=='plb':
            print("\nPlB:\n")
            plb()
            
        elif word=='field':
            print("\nFIELD:\n")
            field()
            
        elif word=='anycraps':
            print("\nANYCRAPS:\n")
            anycraps()
            
        elif word=='twelve':
            print("\nTWELVE:\n")
            twelve()
print("\nBem vindo ao Craps Insper, você inicia com 100 fichas \n")
#corpo principal que desencadeia cada função do jogo
#Faz o jogo rodar até que as fichas acabem
while(fichas>0):
    if(apostar()==False):
        print('ATÉ MAIS')
        break
    else:
        apostas()
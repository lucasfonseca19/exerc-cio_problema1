'''Sorteio e soma'''
import random
dado1=[1,2,3,4,5,6]
dado2=[1,2,3,4,5,6]
fichas=100

'''função apostar ou não(não terminei)'''
def apostar():
    resp=input("\nvocê gostaria de apostar nessa rodada ou sair do jogo?\nDigite'apostar'ou'sair'\n")
    if (resp =='apostar'):
        return True
    else:
def sorteio():
    x=random.choice(dado1)
    y=random.choice(dado2)
    resultado=x+y
    return resultado
    global z
'''funções para modos de jogo'''
def plb():
    global fichas 
    global apostap
    print("o número sorteado é:",z)
    if(z== 7 or z== 11):
        fichas=fichas+apostap 
        print("Agora você tem o total de: {}".format(fichas))
    elif(z== 2 or z== 3 or z== 12):
        fichas=fichas-apostap
        print("Agora você tem o total de: {}".format(fichas))
    elif(z== 4 or z== 5 or z== 6 or z== 8 or z== 9 or z== 10):   
        def loop_point():
            w=sorteio()
            global n
            global fichas
            print("Agora você se encontra na fase point referente ao modo plb pela {}° vez\n".format(n))
            print("O valor {} retirado no priemiro sorteio é seu point".format(z))
            print("O novo valor sorteado é",w)
            n=n+1
            print("agora você possui{}fichas",format(fichas))
            if(w==z):
                fichas=fichas+apostap
                print(fichas)
                return True
            elif(w==7):
                fichas=fichas-apostap
                print("você perdeu tudo!!!")
                return True
            else:
                return False
        while(loop_point()!=True):
            loop_point()
        apostapoint()
    def field():
    global fichas
    global z
    global apostaf
    print("O número sorteado é:",z)
    if(z==5 or z==6 or z==7 or z==8):
        fichas=fichas-apostaf
        print('Você perdeu tudo !!!')
        print("Agora você tem o total de: {}".format(fichas))
    elif(z==3 or z==4 or z==9 or z==10 or z==11):
        fichas=fichas
        print("Você contínua com o total de: {}".format(fichas))
    elif(z==2):
        fichas=fichas+2*apostaf
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas+3*apostaf
        print("Agora você tem o total de: {}".format(fichas))
 def anycraps():
    global fichas
    global z
    global apostaa
    print("o número sorteado é:",z)
    if(z==2 or z==3 or z==12):
        fichas=fichas+7*apostaa
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas-apostaa
        print("Agora você tem o total de: {}".format(fichas))   
        def twelve():
    global fichas
    global z
    global apostat
    print("o número sorteado é:",z)
    if(z==12):
        fichas=fichas+30*apostat
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas-apostat
        print("Agora você tem o total de: {}".format(fichas))

        def apostas():
    tipos=[]
    while True:
        global z
        z=sorteio()
        tipo=input("Você se encontra na fase Come Out\n \nQuais tipos de aposta você gostaria de fazer?\n \n Digite 'plb' e/ou 'field' e/ou'anycraps' e/ou'twelve' separado por virgulas\nQuando terminar de escolher digite 'acabei' ")
        if (tipo =='acabei'):
            break
        tipos.append(tipo)
    for word in tipos:
        global apostaa,apostaf,apostap,apostat
        if word=='plb':
            apostap=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='field':
            apostaf=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))   
        elif word=='anycraps':
            apostaa=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='twelve':
            apostat=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))     
    for word in tipos:
        if word=='plb':
            print("PlB:\n")
            plb()
            
        elif word=='field':
            print("FIELD:\n")
            field()
            
        elif word=='anycraps':
            print("ANYCRAPS:\n")
            anycraps()
            
        elif word=='twelve':
            print("TWELVE:\n")
            twelve()
print("\nBem vindo ao Craps Insper, você inicia com 100 fichas \n")

if (apostar()==True):
    while(fichas>0):
        apostas()
else:
    print("até mais")